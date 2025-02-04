if __name__ == "__main__":
    # Write your solution here

    class Coffee():

        def __init__(self, price, temp):
            """
            :param price: цена кофе
            :param temp: температура кофе
            """
            if not isinstance(price, (int, float)):
                raise TypeError("Цена кофе должна быть числом.")
            if price < 0:
                raise ValueError('Цена должна быть больше нуля')
            self.price = price

            if not isinstance(temp, (int, float)):
                raise TypeError("Температура кофе должна быть числом.")
            if temp < 0:
                raise ValueError('Температура должна быть больше нуля')
            self.temp = temp

        def __str__(self):
            """
            Строчное представление класса
            :return: str
            """
            return f"Кофе за {self.price}. Температура - {self.temp}"

        def __repr__(self):
            return f"{self.__class__.__name__}(price={self.price!r}, temp={self.temp!r})"

        def temp_determine(self):
            """
            Определение по температуре состояние напитка
            :return: str
            """
            if self.temp <= 30:
                return 'Кофе холодный'
            if (self.temp >= 30 and self.temp < 60):
                return 'Кофе теплый'
            if self.temp >= 60:
                return 'Кофе горячий'

        def contraindications(self):
            """
            Выписывает противопоказания
            :return: str
            """
            return 'Напиток не рекомендуется тем, у кого проблемы с сердцем'

    class Cappuchino(Coffee):

        def __init__(self, price, temp):
            super().__init__(price, temp)
            """
            :param price: цена кофе
            :param temp: температура кофе
            """

        def  contraindications(self):
            """
            Перегрузка вызвана по причине того, что не в каждом кофе при приготовлении используется молоко
            Выписывает противопоказания
            :return: str
            """
            return super().contraindications() + ' и людям с непереносимостью лактозы'

        def temp_determine(self):
            """
            Определение по температуре состояние напитка
            :return: str
            """
            return super().temp_determine()


        def __str__(self):
            return super().__str__()

        def __repr__(self):
            return super().__repr__()



else:
    pass

cofe = Cappuchino(5, 50)
print(cofe.temp_determine(),'.', cofe.contraindications())
