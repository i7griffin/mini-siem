from parser import parse_line
from detector import detect_event
from reporter import report_alerts


def main():

    with open("logs/ssh.log", "r") as file:

        for line in file:

            
            event = parse_line(line)

            if event:

                
                alerts = detect_event(event)

                
                if alerts:
                    report_alerts(alerts)


if __name__ == "__main__":
    main()
