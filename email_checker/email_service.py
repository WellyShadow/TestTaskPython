import re

class EmailValidationService:
    @staticmethod
    def validate_email(email):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return False
        allowed_domains = ['example.com', 'gmail.com', 'yahoo.com']  
        domain = email.split('@')[1]
        if domain not in allowed_domains:
            return False
        return True