import unittest
import re

class TestReview(unittest.TestCase): #тест проверки отзыва
    def test_english_review(self):
        with open('reviews.txt', 'r', encoding='utf-8') as file:
            for line in file:
                nickname, review, phone = line.strip().split(',')
                self.assertTrue(re.match(r'^[A-Za-z\s]+$', review), f"Invalid review: {review}") # проверка на то, что отзыв на английском

if __name__ == '__main__':
    unittest.main()

