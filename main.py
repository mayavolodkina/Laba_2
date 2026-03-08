def main():
    print("Выберите режим работы:")
    print("1 — Пользовательский ввод")
    print("2 — Поиск в файле")
    print("3 — Поиск на веб-странице")

    choice = input("Вы выбрали: ")

    if choice == '1':
        check_user_input()
    elif choice == '2':
        fname = input("Введите имя файла: ")
        check_file(fname)
    elif choice == '3':
        url = input("Введите URL: ")
        check_url(url)
    else:
        print("Неверный выбор")