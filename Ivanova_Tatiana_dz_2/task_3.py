"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

user_month = int(input('Укажите месяц в виде целого числа от 1 до 12: '))
# user_month = 5

# 1
# year = {
#     'зима': [12, 1, 2],
#     'весна': [3, 4, 5],
#     'лето': [6, 7, 8],
#     'осень': [9, 10, 11],
# }
#
# for season, months in year.items():
#     if user_month in months:
#         print(f'Введенное вами число {user_month} соответствует времени года: {season}')
#         break
# else:
#     print(f'Вы ввели некорректное число')

# 2
# year = {
#     12: 'зима', 1: 'зима', 2: 'зима',
#     3: 'весна', 4: 'весна', 5: 'весна',
#     6: 'лето', 7: 'лето', 8: 'лето',
#     9: 'осень', 10: 'осень', 11: 'осень',
# }
# if user_month in year.keys():
#     print(f'Введенное вами число {user_month} соответствует времени года: {year.get(user_month)}')
# else:
#     print(f'Вы ввели некорректное число')


# 3
# year = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
# if user_month and user_month <= 12:
#     print(f'Введенное вами число {user_month} соответствует времени года: {year[user_month - 1]}')
# else:
#     print(f'Вы ввели некорректное число')


# 4 ++
year = {
    (12, 1, 2): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень',
}
for months in year:
    if user_month in months:
        print(f'Введенное вами число {user_month} соответствует времени года: {year[months]}')
        break
else:
    print(f'Вы ввели некорректное число')