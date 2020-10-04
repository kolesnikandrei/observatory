

class ListInstance:

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,  # Имя клиентского класса
            id(self),  # Адрес экземпляра
            self.__attr_names(),
        )  # Список пар name=value

    def __attr_names(self):
        result = ''
        for attr in sorted(self.__dict__):  # Словарь атрибутов
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class ListInherited:

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,  # Имя клиентского класса
            id(self),  # Адрес экземпляра
            self.__attr_names(),
        )  # Список пар name=value

    def __attr_names(self):
        result = ''
        for attr in dir(self):  # Передать экземпляр функции dir()
            if attr[:2] == '__' and attr[-2:] == '__':  # Пропустить
                result += '\tname %s=<>\n' % attr  # внутренние имена
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result
