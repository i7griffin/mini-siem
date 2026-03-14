from parser import parse_line

def main():
    with open("logs/ssh.log","r") as file:
        for line in file:
            event = parse_line(line)

            if event:
                print(event)

if __name__ == "__main__":
    main()
