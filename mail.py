from funcs import (
    is_binary_string,
    find_binaries_in_text,
    find_binaries_in_file,
    find_binaries_in_url,
)


def mode_check_input():
    s = input("Введите строку: ")
    if is_binary_string(s):
        print("Строка является двоичным числом.")
    else:
        print("Строка НЕ является двоичным числом.")


def mode_search_in_text():
    text = input("Введите произвольный текст: ")
    binaries = find_binaries_in_text(text)
    if binaries:
        print("Найдены двоичные числа:")
        for b in binaries:
            print(b)
    else:
        print("Двоичных чисел не найдено.")


def mode_search_in_file():
    path = input("Введите путь к текстовому файлу: ")
    try:
        binaries = find_binaries_in_file(path)
    except FileNotFoundError:
        print("Файл не найден.")
        return
    except OSError as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    if binaries:
        print(f"Найдено {len(binaries)} двоичных чисел:")
        for b in binaries:
            print(b)
    else:
        print("В файле двоичных чисел не найдено.")
