from parser import parse_line
from detector import detect_event


def main():
    with open("logs/ssh.log", "r") as file:
        for line in file:

            event = parse_line(line)

            if event:

                alerts = detect_event(event)

                for alert in alerts:
                    print(alert)


if __name__ == "__main__":
    main()
