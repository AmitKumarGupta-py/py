import re

def extract_phone_numbers(text):
    
    pattern = r'\(\d{3}\) \d{3}-\d{4}'

    
    phone_numbers = re.findall(pattern, text)

    return phone_numbers


text = "Call me at (123) 456-7890 or (987) 654-3210."
phone_numbers = extract_phone_numbers(text)
print(phone_numbers)