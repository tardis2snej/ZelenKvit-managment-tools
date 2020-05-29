from UI.main_window import *
import main as main


# окно главного меню
class MainMenu(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_event_listeners()

    def set_event_listeners(self):
        self.send_bill_btn.clicked.connect(self.send_bill_clicked)
        self.prepare_order_btn.clicked.connect(self.order_clicked)
        self.photo_processing_btn.clicked.connect(self.photo_clicked)

    def send_bill_clicked(self):
        main.load_bill_window()

    def order_clicked(self):
        main.load_order_creation()

    def photo_clicked(self):
        main.load_image_processing()
