from PyQt5.QtGui import QGuiApplication
from UI.bill_form import *
import re
from pattern_work import *


# окно для оформления чека, который отправляется клиенту
class BillWindow(QtWidgets.QMainWindow, Ui_BillWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_event_listeners()
        self.orders_list_text = ""

    def set_event_listeners(self):
        self.generate_bill_btn.clicked.connect(self.generate_bill)
        self.copy_btn.clicked.connect(self.copy)

    # скопировать сформированный текст из поля bіll в буфер обмена
    def copy(self):
        if not self.bill.isEnabled():
            return
        text = self.bill.toPlainText()
        if text == "":
            return
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(text)

    # генерирует форму счета
    def generate_bill(self):
        # если ничего не было введено
        if self.orders_list.toPlainText() == "":
            return
        pattern = self.load_bill_pattern()
        if pattern is None:
            return
        # обрабатываем введенный текст и вставляем его в шаблон
        text = self.orders_list.toPlainText()
        lines = text.split("\n")
        # проставляем нумерацию и указанные цены товаров
        prices = []
        for i in range(len(lines)):
            num = str(i + 1) + "."
            if not lines[i].startswith(num):
                lines[i] = num + " " + lines[i]
            # находит часть строки формата "- {число с точкой или запятой} грн."
            price = re.findall("- [\d|\.|,]* грн", lines[i][3:])
            if price:
                for p in price:
                    # вытягиваает из строки само число
                    price_int = float(re.findall(r'\d+(?:\.\d*)?|\.\d+', p.replace(',', '.'))[0])
                    prices.append(price_int)
        final_price = sum(prices)
        # формируем результат форматирования как одну строку
        orders = ""
        for line in lines:
            orders += line + "\n"
        orders = orders[:-2]
        final_text = pattern.replace('{orders}', orders).replace('{sum price}', str(final_price))

        self.bill.setEnabled(True)
        self.bill.setReadOnly(False)
        self.bill.setText(final_text)

    # возвращает шаблон оформления платежа из файла 'bill_pattern.txt', который должен быть в корневой папке
    def load_bill_pattern(self):
        pattern = load_pattern(self, 'bill_pattern.txt')
        if pattern is not None and verify_pattern(self, pattern, ['{orders}', 'sum price'],
                                                  message="Возможно, шаблон составлен неправильно.\n"
                                                          "Убедитесь, что в файле указано {orders} в \n"
                                                          "месте, где нужно разместить строки с заказами\n"
                                                          "и {sum price} в месте для цены"):
            return pattern
