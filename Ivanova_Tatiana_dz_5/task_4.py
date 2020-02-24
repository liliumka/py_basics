"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""

lang_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
}

if __name__ == '__main__':
    try:
        with open('text_4_in.txt', 'r', encoding='utf-8') as f_in, \
                open('text_4_out.txt', 'a', encoding='utf-8') as f_out:
            for row in f_in:
                key, value = row.strip().split(' — ')
                new_row = row.replace(key, lang_dict[key] if key in lang_dict else 'empty')
                f_out.write(f'{new_row}')
    except FileNotFoundError as e:
        print(f'no file: {e}')
    except FileExistsError as e:
        print(f'file already exists: {e}')
    except Exception as e:
        print(f'strange error: {e}')
