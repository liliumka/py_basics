"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

user = {
    'first_name': 'Raul',
    'last_name': 'Fernando',
    'birth_year': '1980',
    'city': 'Paris',
    'email': 'mail@pisem.net',
    'phone': '123456',
}

user_2 = {
    'first_name': '',
    'last_name': '',
    'birth_year': '',
    'city': '',
    'email': '',
    'phone': '',
}


# Вариант 1
def user_info_min(**kwargs):
    """Краткий вывод всех полученных именованных параметров, описвающих данные пользователя."""
    return ', '.join([f'{key} - {val}' for key, val in kwargs.items()])


print(user_info_min(**user))
print(user_info_min(**user_2))
print('-' * 80)


# Вариант 2
def user_info(**kwargs):
    """
    Формирование строки с данными пользователя.

    В выводе участвуют только конкретные параметры. Если какой-то параметр не передан, он заменяется некой фразой.
    """
    first_name = kwargs.get('first_name')
    last_name = kwargs.get('last_name')
    birth_year = kwargs.get('birth_year')
    city = kwargs.get('city')
    email = kwargs.get('email')
    phone = kwargs.get('phone')

    result = f'Гражданин {first_name} {last_name} ' if first_name or last_name else 'Неизвестный Гражданин '
    result += f'{birth_year} года рождения, ' if birth_year else 'неопределенного возраста, '
    result += f'проживает в городе {city}. ' if city else 'без определенного места жительства. '
    result += f'Адрес для электронных писем: {email}, ' if email else 'Не имеет адреса электронной почты, '
    result += f'контактный телефон: {phone}.' if phone else 'телефон давно заблокирован и забыт.'
    return result


print(user_info(**user))
print(user_info(**user_2))
print('-' * 80)


# Вариант 3
def user_info_2(first_name, last_name, birth_year, city, email, phone):
    """
    Формирование строки с данными пользователя.

    :param string first_name: Имя
    :param string last_name: Фамилия
    :param string birth_year: год рождения
    :param string city: город проживания
    :param string email: электронный адрес
    :param string phone: телефон
    :return: string
    """
    return f'Гражданин {first_name or "-"} {last_name or "-"} {birth_year or "-"} года рождения, ' \
           f'проживает в городе {city or "-"}. Адрес для электронных писем: {email or "-"}, ' \
           f'контактный телефон: {phone or "-"}.'


print(user_info_2(**user))
print(user_info_2(**user_2))
