import json
from datetime import datetime

ALERT_FILE = "alerts.json"


def report_alerts(alerts):

    for alert in alerts:

        # Add timestamp
        alert["timestamp"] = datetime.now().isoformat()

        # Print alert (optional)
        print(alert)

        # Load existing alerts
        try:
            with open(ALERT_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

        # Add new alert
        data.append(alert)

        # Save back to file
        with open(ALERT_FILE, "w") as f:
            json.dump(data, f, indent=4)
