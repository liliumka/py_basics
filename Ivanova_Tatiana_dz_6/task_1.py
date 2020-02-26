"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.__counter = 0
        self.__scheme = ('red', 'yellow', 'green')
        self.__time_mode = {
            'red': 7,
            'yellow': 2,
            'green': 5
        }

    def running(self, new_color=''):
        """
        Запускает работу светофора с режима, указанного в new_color или атрибуте класса __color.

        При вызове метода running() без параметров, светофор запускает работу с режима, указанного в self.__color.
        Получив параметр new_color, светофор попытается запустить работу с указанного режима, либо выдаст исключение.

        Светофор отключится, отработав несколько режимов (if self.__counter < 7).

        :param str new_color:
        :return:
        """
        color = self.__color  # не стала добавлять get и set методы
        sec = self.__time_mode.get(color)

        if new_color and isinstance(new_color, str):
            if new_color not in self.__scheme:
                raise ValueError('Ошибка! Указан некорректный режим работы!')
            else:
                if new_color == self.__color:
                    raise ValueError('Ошибка! Светофор уже находится в данном режиме!')
                elif new_color != self.__get_next_color(color):
                    raise ValueError('Ошибка! Требуемый режим не соответвует последовательности смены режимов!')
                else:
                    self.__change_color(color)
        else:
            print(f'загорелся {color.upper()}:')
            self.__countdown(sec)
            # светофор работает в течении ограниченного времени, скажем 5 раз меняется цвет и отключается
            if self.__counter < 5:
                # этот метод меняет цвет и заново запускает текущий
                self.__change_color(color)
            else:
                print(f'светофор отключился')

    def __countdown(self, sec):
        """
        Запускаем таймер обратного отсчета времени работы текущего режима.

        :param int sec:
        :return:
        """
        for s in range(-sec, 0):
            print(abs(s))
            sleep(1)

    def __change_color(self, color):
        """
        Меняем цвет на следующий после color и продолжаем работу светофора.
        Также увеличиваем счетчик смены режимов работы.

        :param str color:
        :return:
        """
        self.__color = self.__get_next_color(color)
        self.__counter += 1
        self.running()

    def __get_next_color(self, color):
        """
        Получаем из кортежа следующий за color цвет, либо первый, если color является последним элементом кортежа.

        :param str color:
        :return:
        """
        current_idx = self.__scheme.index(color)
        next_idx = current_idx + 1 if len(self.__scheme) - 1 != current_idx else 0
        return self.__scheme[next_idx]


if __name__ == '__main__':
    lighter = TrafficLight()

    # вызов без параметров запустит светофор с заданного в атрибуте цвета
    lighter.running()

    # вызов с параметром попытается запустить светофор с указанного режима, либо выдаст исключение
    # lighter.running('yellow')

    # здесь будут ошибки, т.к. по умолчанию режим работы начинается с красного, а следующий - желтый
    # lighter.running('green')
