import re

def extract_emails(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    
    emails = re.findall(pattern, text)

    
    unique_emails = set(emails)
    count = len(unique_emails)

    return unique_emails, count


file_path = 'example.txt'
unique_emails, count = extract_emails(file_path)
print(f"Unique Email Addresses: {unique_emails}")
print(f"Count: {count}")
