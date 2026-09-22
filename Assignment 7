import re

def find_emails(text):
    pattern = r'\b[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}\b'
    matched_emails = re.findall(pattern, text)
    return matched_emails

if __name__ == "__main__":
    input_text = input("Enter the text to search for email addresses: ")
    results = find_emails(input_text)
    print("Extracted Email Addresses:", results)
