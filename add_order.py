from PyQt5 import QtWidgets
from PyQt5.QtGui import QGuiApplication
from UI.add_order_form import Ui_AddOrder
from pattern_work import *
from table import *


# окно для оформления оплаченного заказа и добавления его в архив
class OrderWindow(QtWidgets.QMainWindow, Ui_AddOrder):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_event_listeners()
        self.orders_text_list = []

    def add_event_listeners(self):
        self.generate_order_btn.clicked.connect(self.generate_order)
        self.copy_to_clipboard_btn.clicked.connect(self.copy)
        self.add_to_archive_btn.clicked.connect(self.add_to_archive)
        self.add_pos_btn.clicked.connect(self.add_pos)

    # добавить строку для предмета в заказе
    def add_pos(self):
        order_pos = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(order_pos)
        self.orders_text_list.append(order_pos)

    # сгенерировать текст по шаблону
    def generate_order(self):
        values = {
            '{order id}': str(self.order_num_fld.value()),
            '{money sum}': str(self.money_transferred_fld.value()),
            '{payment time}': self.pay_date_fld.text(),
            '{city}': self.city_fld.text(),
            '{post number}': self.post_num_fld.text(),
            '{client name}': self.client_name_fld.text(),
            '{client telephone}': self.telephone_fld.text(),
            '{orders}': ''
        }
        pattern = load_pattern(self, 'order_pattern.txt')
        if pattern is None or not verify_pattern(self, pattern, values.keys(),
                                                 message="Возможно, шаблон составлен неправильно.\n"
                                                         "Убедитесь, что в файле указаны метки"
                                                         "{order id}, {money sum}, {payment time}, {orders}, {city},"
                                                         "{post number}, {client name}, {client telephone}"):
            return

        values['{orders}'] = self.get_orders_list()

        for key in values:
            if values[key] == '':
                self.generated_text_area.setText(
                    "Заполните все поля обязательной информации, чтобы сгенерировать текст")
                return
            pattern = pattern.replace(key, values[key])
        self.generated_text_area.setText(pattern)
        self.generated_text_area.setEnabled(True)
        self.generated_text_area.setReadOnly(False)

    # получить все вписанные товары одной строкой
    def get_orders_list(self):
        orders = ''
        i = 1
        for order in self.orders_text_list:
            if order.toPlainText() != '':
                orders += str(i) + ". " + order.toPlainText() + "\n"
                i += 1

        orders = orders[:-1]
        return orders

    # скопировать в буфер обмена
    def copy(self):
        if not self.generated_text_area.isEnabled():
            return
        text = self.generated_text_area.toPlainText()
        if text == "":
            return
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(text)

    # добавление введенных данных в таблицу
    def add_to_archive(self):
        try:
            archive = Table('orders_archive.xlsx')
        except BaseException as e:
            QMessageBox.critical(None, "Ошибка", e.__str__(), QMessageBox.Cancel)
            return
        req_values = {
            'order num': self.order_num_fld.value(),
            'pay date': self.pay_date_fld.text(),
            '{city}': self.city_fld.text(),
            '{post number}': self.post_num_fld.text(),
            'name': self.client_name_fld.text(),
            'telephone': self.telephone_fld.text(),
            '{orders}': [order.toPlainText() for order in self.orders_text_list]
        }
        for key in req_values.keys():
            if req_values[key] == '':
                QMessageBox.critical(self, "Недостаточно данных", "Заполните все поля обязательной информации", QMessageBox.Ok)
                return

        values = {
            'where from short': self.where_from_short_fld.text(),
            'viber group': self.viber_group_fld.currentText(),
            'provider price': float(self.povider_price_fld.text().replace(',', '.')),
            'discount': float(self.provider_discount_fld.text().replace(',', '.')),
            'sell price': float(self.selling_price_fld.text().replace(',', '.')),
            'income': 0,
            'adress': req_values['{city}'] + "; отделение почты: " + req_values['{post number}'],
            'more contacts': self.more_contacts_fld.text(),
            'notes': self.notes_fld.toPlainText()
        }
        values['income'] = values['sell price'] - (values['provider price'] - values['provider price']*values['discount']/100)
        values.update(req_values)

        row = archive.get_next_empty_row()
        columns = archive.get_columns()
        try:
            for column in columns.keys():
                if column in values.keys():
                    archive.insert_into_cell(columns[column], row, values[column])
            for order in values['{orders}']:
                archive.insert_into_cell(columns['order'], row, order)
                row += 1
            archive.save()
            QMessageBox.information(self, "Успех", "Операция совершена успешно")
        except PermissionError:
            QMessageBox.critical(self, "Доступ запрещен", "Невозможно получить доступ к файлу.\n "
                                                          "Возможно, он используется другой программой.\n")
