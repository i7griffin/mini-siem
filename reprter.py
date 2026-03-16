def report_alerts(alerts):

    for alert in alerts:


        if alert["type"] == "BRUTE_FORCE":
            print("⚠ Possible Brute Force Attack Detected")
            print(f"IP Address : {alert['ip']}")
            print(f"Attempts   : {alert['attempts']}")

        elif alert["type"] == "LOGIN_SUCCESS":
            print("✓ Successful Login Detected")
            print(f"User       : {alert['user']}")
            print(f"IP Address : {alert['ip']}")

        print(f"Message    : {alert['message']}")

        print("======================================\n")
