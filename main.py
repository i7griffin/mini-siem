import subprocess
from parser import parse_line
from detector import detect_event
from reporter import report_alerts


def stream_ssh_logs():
    """Subprocess is generally a module which is used to direct and pipe the output of one command to another""" 

    process = subprocess.Popen(
        ["journalctl", "-f", "-n", "0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    """yield is used to produce a iterator in the group of results to parse and work on each one of them"""
    for line in process.stdout:
        yield line


def main():

    print(" Mini SIEM Started")
    print(" Monitoring SSH logs in real time...\n")

    for line in stream_ssh_logs():

        """i used the below line to check whether there is problem in producing the logs or int he parser code"""
        #print(line)

        event = parse_line(line)

        if event:

            alerts = detect_event(event)

            if alerts:
                report_alerts(alerts)


if __name__ == "__main__":
    main()
