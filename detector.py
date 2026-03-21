import time
from collections import defaultdict

failed_attempts = defaultdict(list)

THRESHOLD = 2
WINDOW = 60

def detect_event(event) :


    alerts = []
    ip = event["ip"]
    now = time.time()

    # FAILED LOGIN
    if event["event"] == "failed":

        failed_attempts[ip].append(now)

        # keep only recent attempts
        failed_attempts[ip] = [
            t for t in failed_attempts[ip]
            if now - t <= WINDOW
        ]

        if len(failed_attempts[ip]) >= THRESHOLD:
            alerts.append({
                "type": "BRUTE_FORCE",
                "ip": ip,
                "attempts": len(failed_attempts[ip]),
                "message": f"Brute force detected from {ip}"
            })

    # SUCCESS LOGIN
    elif event["event"] == "accepted":

        alerts.append({
            "type": "LOGIN_SUCCESS",
            "user": event["user"],
            "ip": ip,
            "message": f"User {event['user']} logged in"
        })

        # correlation: success after brute force
        if len(failed_attempts[ip]) >= THRESHOLD:
            alerts.append({
                "type": "COMPROMISED_ACCOUNT",
                "user": event["user"],
                "ip": ip,
                "message": "Login after brute force → possible compromise"
            })

        # reset after success
        failed_attempts[ip] = []

    return alerts
