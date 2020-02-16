"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

# user_text = input('Введите несколько слов из латинских букв в нижнем регистре, разделенных пробелом: ')
user_text = 'lorem ipsum dolor sit amet consectetur adipiscing elit'


# Вариант 1
def func_title(text):
    """
    Возращает строку, в которой все слова с прописной первой буквой.

    К каждому слову применяется метод capitalize.

    :param str text:
    :return:
    """
    text_as_list = text.split()
    return ' '.join(map(str.capitalize, text_as_list))


print(user_text)
print(func_title(user_text))
print('-' * 80)


# Вариант 2
def func_title_2(text):
    """
    Возращает строку, в которой все слова с прописной первой буквой.

    В каждом слове заменяется первый символ строчной буквы, на символ прописной буквы.

    :param str text:
    :return:
    """
    text_as_list = text.split()
    return ' '.join(map(lambda word: f'{chr(ord(word[0]) ^ 32)}{word[1:]}', text_as_list))


print(user_text)
print(func_title_2(user_text))
