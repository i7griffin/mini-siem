import re

pattern = r"(Failed|Accepted) password for (invalid user )?([a-zA-Z0-9._-]+) from ([\d\.:]+)"

def parse_line(line):

    """i used the below  line because ihelps me to filter just only the ssh logs instead of getting allt he logs"""
    if "Failed password" not in line and "Accepted password" not in line:
        return None

    match = re.search(pattern, line)

    if match:
        event = match.group(1)
        user = match.group(3)
        ip = match.group(4)

        return {
            "event": event.lower(),
            "user": user,
            "ip": ip
        }

    return None
