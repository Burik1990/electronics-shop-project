from src.item import Item


class MixinLang:
    '''Класс для хранения и изменения раскладки клавиатуры'''
    Language = 'EN'

    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = 'RU'
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):
    '''Класс для товара “клавиатура”'''

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
