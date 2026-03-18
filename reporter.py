def report_alerts(alerts):

    for alert in alerts:

        if alert["type"] == "BRUTE_FORCE":
            print("⚠ BRUTE FORCE DETECTED")
            print("IP:", alert["ip"])
            print("Attempts:", alert["attempts"])

        elif alert["type"] == "LOGIN_SUCCESS":
            print("✓ LOGIN SUCCESS")
            print("User:", alert["user"])
            print("IP:", alert["ip"])

        elif alert["type"] == "COMPROMISED_ACCOUNT":
            print(" ACCOUNT COMPROMISED")
            print("User:", alert["user"])
            print("IP:", alert["ip"])

        print("Message:", alert["message"])
        print("----------------------------------")
