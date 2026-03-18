import subprocess
from parser import parse_line
from detector import detect_event
from reporter import report_alerts


def stream_ssh_logs():

    process = subprocess.Popen(["journalctl","-u","ssh","-f","-n",'0'],stdout=subprocess.PIPE , stderr=subprocess.PIPE , text=True , bufsize=1)

    for line in process.stdout : 

        yield line 


def main():
    print("MINI SIEM started")
    print("Monitoring logs in real time")

    for line in stream_ssh_logs() :

	event = parse_line(line) 

	if event :

	    alerts = detect_event(event)

	    if alerts :

		report_alerts(alerts)


if __name__ == "__main__":
    main()
