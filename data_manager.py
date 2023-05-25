import re

VALIDATION_PATTERNS = {
    "name": r'[A-Z]\w+',
    "dob": r'\d{2}\s?\w+\s?\d{4}',
    "user_additional_info": r'.+',
    "address": r'.+',
    "usermail": r'[\w\.-_]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}',
    "tel": r'\d?-?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
}


class DataInterpreter:
    def __init__(self):
        self.__result_dict = [("name", "dob", "user_additional_info", "address", "tel", "usermail")]
        self.__not_valid_data = []

    def add_data(self, data):
        print(data)
        for row in data:
            """name, date, nationality, address, tel, email"""
            self.__result_dict.append((self.validate(value=row[0], kay="name"),
                                       self.validate(value=row[1], kay="dob"),
                                       self.validate(value=row[2], kay="user_additional_info"),
                                       self.validate(value=row[3], kay="address"),
                                       self.validate(value=row[4], kay="tel"),
                                       self.validate(value=row[5], kay="usermail"),
                                       ))

    def validate(self, value, kay):
        """Return valid values or empty string"""
        if re.match(pattern=VALIDATION_PATTERNS.get(kay), string=str(value)):
            return value
        else:
            self.__not_valid_data.append(f"{kay}: {value}")
            return ""

    @property
    def get_final_values(self):
        return self.__result_dict

    @property
    def get_not_valid_data(self):
        return self.__not_valid_data
