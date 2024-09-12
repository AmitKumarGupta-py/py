import re

def find_urls(text):
    # Regular expression pattern to match URLs
    pattern = r'https?://\S+'

    # Find all URLs in the text
    urls = re.findall(pattern, text)

    return urls

# Example usage
text = "Visit (https://www.google.com/) for search and (https://www.Example.com/) for examples."
urls = find_urls(text)
print(urls)