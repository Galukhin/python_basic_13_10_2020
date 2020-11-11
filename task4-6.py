"""

"""


class BalanceError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LenError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:

    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price


class Printer(OfficeEquipment):

    def __init__(self, brand: str, model: str, price: float, color_print: bool, type_print: str):
        super().__init__(brand, model, price)
        self.color_print = color_print
        self.type_print = type_print


class Xerox(OfficeEquipment):

    def __init__(self, brand: str, model: str, price: float, type_xerox: str):
        super().__init__(brand, model, price)
        self.type_xerox = type_xerox


class Scanner(OfficeEquipment):

    def __init__(self, brand: str, model: str, price: float, type_scanner: str):
        super().__init__(brand, model, price)
        self.type_scanner = type_scanner


class Warehouse:

    def __init__(self, name: str):
        self.name = name
        self.items = {}

    def receive(self, *args):
        """
        Оформляет получение товара на склад
        :param args: список объектов офисной техники
        :return: None
        """
        for itm in args:
            if isinstance(itm, (type(Printer), type(Xerox), type(Scanner))):
                raise TypeError('Неверные объекты для поставки на склад')
            qty = self.items.setdefault(type(itm).__name__)
            if qty is None:
                self.items.update({type(itm).__name__: 1})
            else:
                self.items.update({type(itm).__name__: qty + 1})

    def send(self, name: str, department: str, qty: int):
        """
        Оформляет передачу товаров в подразделение
        :param name: имя класса объекта
        :param department: наименование подразделения
        :param qty: количество
        :return: None
        """
        balance = self.items.setdefault(name)
        if balance is None:
            raise ValueError('Такого товара на складе нет')
        if balance < qty:
            raise BalanceError('Товара на складе недостаточно')
        self.items.update({name: balance - qty})
        print(f'В отдел {department} передано {qty} {name}')


if __name__ == '__main__':
    printers = []
    xeroxes = []
    scanners = []
    idx = 0
    while idx < 10:
        printers.append(Printer('Canon', 'TS304', 4000, True, 'laser'))
        xeroxes.append(Xerox('Xerox', 'WorkCentre 3025', 17000, 'MFD'))
        scanners.append(Scanner('Epson', 'Perfection V19', 5600, 'tablet'))
        idx += 1
    my_warehouse = Warehouse('my_warehouse')
    my_warehouse.receive(*printers)
    my_warehouse.receive(*xeroxes)
    my_warehouse.receive(*scanners)
    print(my_warehouse.items)
    print('Подайте заявку на получение оргтехники в формате: "name department qty"')
    while True:
        try:
            user_request = input('>>>').split()
            if len(user_request) != 3:
                raise LenError('Неверный формат заявки!')
        except LenError as err3:
            print(err3)
            continue
        try:
            user_request[2] = int(user_request[2])
        except ValueError:
            print('Неверно указано количество!')
            continue
        try:
            my_warehouse.send(*user_request)
        except ValueError as err1:
            print(err1)
            continue
        except BalanceError as err2:
            print(err2)
            continue
        break
    print(my_warehouse.items)
