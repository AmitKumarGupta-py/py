import re

def is_valid_ipv4(ip):
    
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    
    if re.match(pattern, ip):
        return True
    else:
        return False


ip = "192.168.1.1"
if is_valid_ipv4(ip):
    print(f"{ip} is a valid IPv4 address")
else:
    print(f"{ip} is not a valid IPv4 address")