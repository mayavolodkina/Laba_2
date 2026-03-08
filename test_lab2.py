import unittest
import re
from main import get_pattern


class TestRegex(unittest.TestCase):
    def setUp(self):
        self.pattern = get_pattern()
        print("--- Запуск теста ---")

    def test_valid_emails(self): #тест на правильных имейлах
        valid_emails = [
            "test@example.com",
            "user.name@domain.org",
            "login+tag@mail.ru",
            "info@company.co.uk",
            "a@b.c"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertIsNotNone(
                    self.pattern.fullmatch(email),
                    f"Ошибка: '{email}' должен быть распознан как праильный"
                )

    def test_invalid_emails(self): #тест на неправильных имейлах
        invalid_emails = [
            "plainaddress",
            "@missinglocal.com",
            "missing@.com",
            "missing@domain.",
            "spaces @email.com",
            "no-at-sign.com",
            "double@@domain.com"
        ]

        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertIsNone(
                    self.pattern.fullmatch(email),
                    f"Ошибка: '{email}' не должен быть распознан как правильный"
                )

    def test_find_in_text(self): #имейл в тексте
        text = "Контакты: support@mail.com и sales@company.org для связи."
        expected_count = 2

        matches = self.pattern.findall(text)

        self.assertEqual(
            len(matches), expected_count,
            f"Ожидалось {expected_count} совпадений, найдено {len(matches)}"
        )
        self.assertIn("support@mail.com", matches)
        self.assertIn("sales@company.org", matches)

    def test_empty_input(self): #пустая сторка
        text = ""
        matches = self.pattern.findall(text)
        self.assertEqual(matches, [])

    def test_no_matches(self): #без имейлов
        text = "Здесь нет почт."
        matches = self.pattern.findall(text)
        self.assertEqual(len(matches), 0)

    if __name__ == '__main__':
        # verbosity=2 делает вывод подробным (показывает имя каждого теста)
        unittest.main(verbosity=2)