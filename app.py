from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

ALERT_FILE = "alerts.json"


def load_alerts():
    try:
        with open(ALERT_FILE, "r") as f:
            return json.load(f)
    except:
        return []


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/alerts")
def get_alerts():
    return jsonify(load_alerts())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
