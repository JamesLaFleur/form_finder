import re

class Field_validator:
    email_pattern = r'^\S+@\w+.\w{2,4}$'
    phone_pattern =  r'^\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$'
    date_pattern_ru = r'^\d\d\.\d\d\.\d{4}$'
    date_pattern_en = r'^\d{4}\-\d\d\-\d\d$'

    def is_email(self, string):
        return re.fullmatch(self.email_pattern, string)
    
    def is_date(self, string):
        return re.fullmatch(self.date_pattern_ru, string) or re.fullmatch(self.date_pattern_en, string)
    
    def is_phone(self, string):
        return re.fullmatch(self.phone_pattern, string)
    
    def get_field_type(self, string):
        if self.is_date(string):
            return "date"
        if self.is_phone(string):
            return "phone"
        if self.is_email(string):
            return "email"

        return "text"