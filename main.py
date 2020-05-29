import sys
import main_menu
import bill
from ProcessImageWindow import *
from add_order import *

# хранит все открытые окна, чтобы они не закрывались, когда исчезают из областей видимости запустивших их функций
windows = []


def main():
    app = QtWidgets.QApplication(sys.argv)
    load_main_menu()
    app.exec_()


# запуск главного меню
def load_main_menu():
    window = main_menu.MainMenu()  # Create main window
    window.show()
    windows.append(window)


# запуск окна со счетом
def load_bill_window():
    window = bill.BillWindow()
    window.show()
    windows.append(window)


# запуск окна с созданием подтвержденного заказа
def load_order_creation():
    window = OrderWindow()
    window.show()
    windows.append(window)


# запуск окна с обработкой картинок
def load_image_processing():
    # для работы нужна папка temp в корневом каталоге
    if not os.path.exists("temp"):
        os.mkdir("temp")
    window = ProcessImageWindow()
    window.show()
    windows.append(window)


if __name__ == "__main__":
    main()
