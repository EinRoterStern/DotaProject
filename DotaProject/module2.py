import unittest
import re


def validate_phone_number(phone):
    
    pattern = r'^\+\d{1}\s\d{3}\s\d{3}\s\d{2}\s\d{2}$' 
    return re.match(pattern, phone) is not None

class PhoneNumberValidationTest(unittest.TestCase):
    def test_phone_number_format(self):
        
        with open('reviews.txt', 'r', encoding='utf-8') as file: 
            for line in file:
                nickname, review, phone = line.strip().split(',')
 
                self.assertTrue(validate_phone_number(phone))

if __name__ == '__main__':
    unittest.main()