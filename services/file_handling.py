import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_page = [',', '!', '?', ':', ';', '.']
    for i in range(0, size):
        if (start + size) < len(text):
            text_page = text[start: size + start - i]
            if text_page[-1] in end_page:
                if len(text) > (start + size) and text[start + size - i] != '.':
                    break
        else:
            text_page = text[start:]
    size_page = len(text_page)
    return (text_page, size_page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding="UTF-8") as file_in:
        text = file_in.read()
        page = 1
        start = 0
    while start < len(text):
        content = _get_part_text(text, start, PAGE_SIZE)
        text_page = content[0]
        size_page = content[1]
        text_page = text_page.lstrip()
        book[page] = text_page
        page += 1
        start += size_page


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
