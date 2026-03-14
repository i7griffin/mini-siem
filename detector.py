from collections import defaultdict

# store failed attempts per IP
failed_attempts = defaultdict(int)

# threshold for brute force detection
THRESHOLD = 3


def detect_event(event):
    """
    Takes parsed event from parser.py and checks for suspicious activity
    """

    alerts = []

    if event["event"] == "failed":
        ip = event["ip"]

        failed_attempts[ip] += 1

        if failed_attempts[ip] >= THRESHOLD:
            alerts.append({
                "type": "BRUTE_FORCE",
                "ip": ip,
                "attempts": failed_attempts[ip],
                "message": f"Possible brute force attack from {ip}"
            })

    if event["event"] == "accepted":
        user = event["user"]
        ip = event["ip"]

        alerts.append({
            "type": "LOGIN_SUCCESS",
            "user": user,
            "ip": ip,
            "message": f"Successful login for {user} from {ip}"
        })

    return alerts
