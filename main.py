import re
import requests


def get_pattern():
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.compile(pattern)

def check_input():
    text = input("Введите текст для поиска: ")
    matches = get_pattern().findall(text)
    if matches:
        print(f"Найден имейл: {matches}")
    else:
        print("Ничего не найдено.")
    return matches

def check_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()

        pattern = get_pattern()
        matches = pattern.findall(text)

        print(f"В файле {filename} найдено: {matches}")
        return matches
    except FileNotFoundError:
        print("Файл не найден!")
        return []

def check_url(url):
    try:
        # Загружаем содержимое страницы
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки (404, 500)

        text = response.text
        pattern = get_pattern()
        matches = pattern.findall(text)

        print(f"На странице {url} найдено: {matches}")
        return matches
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

def main():
    print("Выберите режим работы:")
    print("1 — Пользовательский ввод")
    print("2 — Поиск в файле")
    print("3 — Поиск на веб-странице")

    choice = input("Вы выбрали: ")

    if choice == '1':
        check_input()
    elif choice == '2':
        filename = input("Введите имя файла: ")
        check_file(filename)
    elif choice == '3':
        url = input("Введите URL: ")
        check_url(url)
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()