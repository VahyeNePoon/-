import doctest

class Chair:
    def __init__(self, height: int, weight: int, material: str):
        """

        :param height: высота стула
        :param weight: ширина стула
        :param material: материал стула

        Примеры:
        >>> chair = Chair(100, 40, 'metal') #инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError('Высота стула должна быть тип int или float')
        if height <= 0:
            raise ValueError('Высота стула должна быть положительным числом')
        self.height = height

        if not isinstance(weight, (int, float)):
            raise TypeError('Ширина стула должна быть тип int или float')
        if weight <= 0:
            raise ValueError('Ширина стула должна быть положительным числом')
        self.weight = weight

        if not isinstance(material, str):
            raise TypeError('Материал стула должен быть типом данным string')
        self.material = material



    def wood_chair(self) -> bool:
        """
        Функция проверяет, является ли стул деревянным или нет



        :return: Является ли стул деревянным
        Пример:
        >>> chair = Chair(100, 40, 'metal')
        >>> chair.wood_chair()
        """
        ...

    def plastic_chair(self) -> bool:
        """
        Функция проверяет, является ли стул пластиковым или нет



        :return: Является ли стул пластиковым
        Пример:
        >>> chair = Chair(100, 40, 'metal')
        >>> chair.plastic_chair()
        """
        ...

    def metal_chair(self) -> bool:
        """
        Функция проверяет, является ли стул металлическим или нет



        :return: Является ли стул металлическим
        Пример:
        >>> chair = Chair(100, 40, 'metal')
        >>> chair.metal_chair()
        """
        ...

class Pan:
    def __init__(self, color: str, length: int, material: str):
        """

        :param color: цвет ручки
        :param length: длина ручки
        :param material: материал ручки

        Пример:
        >>> pan = Pan('black', 10, 'metal')
        """
        if not isinstance(color, str):
            raise TypeError("цвет ручки должен быть типа str")
        self.color = color

        if not isinstance(length, (int,float)):
            raise TypeError('Длина ручки должна быть указана как int или float')
        if length <= 0:
            raise ValueError('длина ручки должна быть больше нуля')
        self.length = length

        if not isinstance(material, str):
            raise TypeError('Материал ручки должен быть типа str')

    def color_determine(self):
        """
        Функция проверяет, какой цвет у ручки

        :return: цвет ручки
        Примеры:
        >>> pan = Pan('black', 10, 'metal')
        >>> pan.color_determine()
        """
        ...

    def material_determine(self):
        """
        Функция определяет материал ручки
        :return: материал ручки
        Примеры:
        >>> pan = Pan('black', 10, 'metal')
        >>> pan.material_determine()
        """
        ...

    def length_determine(self):
        """
        Функция определяет, насколько ручка длинная относительно средней длины ручек
        :return: одно из значений: длинная, короткая или средняя
        """
        ...

class Bottle:
    def __init__(self, height: int, material: str, filling: str):
        """

        :param height: Высота бутылки
        :param material: материал,из которого сделана бутылка
        :param filling: наполнение бутылки
        Примеры:
        >>> bottle = Bottle(50, 'plastic', 'water')
        """
        if not isinstance(height, (int, float)):
            raise TypeError('Высота стула должна быть тип int или float')
        if height <= 0:
            raise ValueError('Высота стула должна быть положительным числом')
        self.height = height

        if not isinstance(material, str):
            raise TypeError('Материал бутылки должен быть типа str')
        self.material = material

        if not isinstance(filling, str):
            raise TypeError('Наполнение бутылки должно быть типа str')
        self.filling = filling

    def bottle_volume(self):
        """
        Функция по высоте бутылки узнает какой объем у бутылки
        :return: значение объема
        Примеры:
        >>> bottle = Bottle(50, 'plastic', 'water')
        >>> bottle.bottle_volume()
        """
        ...

    def bottle_material(self):
        """
        Функция показывает материал бутылки
        :return: материал бутылки
        Примеры:
        >>> bottle = Bottle(50, 'plastic', 'water')
        >>> bottle.bottle_material()
        """
        ...
    def bottle_filling(self):
        """
        Функция показывает, какое содержимое у бутылки
        :return: содержимое бутылки
        Примеры:
        >>> bottle = Bottle(50, 'plastic', 'water')
        >>> bottle.bottle_filling()
        """
        ...

# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    bottle = Bottle(50, 'plastic', 'water')
    pass
    # TODO работоспособность экземпляров класса проверить с помощью doctest





















