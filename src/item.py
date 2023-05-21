import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(str_num: str):
        '''Возвращаем число из числа-строки'''
        return int(float(str_num))


    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        '''Инициализируем экземпляры класса `Item` данными из файла _src/items.csv_'''
        cls.all.clear()
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        '''Отображение информации об объекте класса в режиме отладки (для разработчиков)'''
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        '''Отображение информации об объекте класса для пользователей'''
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
             print('Длина наименования товара превышает 10 символов')


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return  self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None
