import re

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_emails(text):
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)

def extract_phone_numbers(text):
    return re.findall(r"\+?\d[\d\s\-()]{7,}\d", text)