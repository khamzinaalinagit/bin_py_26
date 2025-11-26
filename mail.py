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
