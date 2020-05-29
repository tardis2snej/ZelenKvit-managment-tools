# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bill_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BillWindow(object):
    def setupUi(self, BillWindow):
        BillWindow.setObjectName("BillWindow")
        BillWindow.resize(1100, 500)
        self.centralwidget = QtWidgets.QWidget(BillWindow)
        self.centralwidget.setStyleSheet("#centralwidget { background-color: qlineargradient(spread:pad, x1:0.084, y1:0.329545, x2:0.901, y2:0.551136, stop:0 rgba(221, 255, 199, 255), stop:0.232451 rgba(187, 255, 184, 255), stop:0.680092 rgba(221, 255, 164, 255), stop:1 rgba(145, 255, 161, 255)); }")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.orders_list = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.orders_list.setFont(font)
        self.orders_list.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.orders_list.setObjectName("orders_list")
        self.verticalLayout.addWidget(self.orders_list)
        self.generate_bill_btn = QtWidgets.QCommandLinkButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.generate_bill_btn.setFont(font)
        self.generate_bill_btn.setStyleSheet("font: 12pt \"Garamond\";")
        self.generate_bill_btn.setObjectName("generate_bill_btn")
        self.verticalLayout.addWidget(self.generate_bill_btn)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bill = QtWidgets.QTextEdit(self.widget_2)
        self.bill.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.bill.setFont(font)
        self.bill.setReadOnly(True)
        self.bill.setObjectName("bill")
        self.verticalLayout_2.addWidget(self.bill)
        self.copy_btn = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.copy_btn.setFont(font)
        self.copy_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(114, 201, 113, 137), stop:0.264151 rgba(116, 234, 105, 211), stop:0.496115 rgba(188, 224, 133, 124), stop:0.778024 rgba(163, 228, 112, 220), stop:1 rgba(214, 255, 152, 182));")
        self.copy_btn.setObjectName("copy_btn")
        self.verticalLayout_2.addWidget(self.copy_btn)
        self.horizontalLayout.addWidget(self.widget_2)
        BillWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BillWindow)
        self.statusbar.setObjectName("statusbar")
        BillWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BillWindow)
        QtCore.QMetaObject.connectSlotsByName(BillWindow)

    def retranslateUi(self, BillWindow):
        _translate = QtCore.QCoreApplication.translate
        BillWindow.setWindowTitle(_translate("BillWindow", "Выставить счет для оплаты"))
        self.label.setText(_translate("BillWindow", "Наименования товаров - каждое с новой строки:"))
        self.generate_bill_btn.setText(_translate("BillWindow", "Сгенерировать счет"))
        self.generate_bill_btn.setShortcut(_translate("BillWindow", "Shift+Return"))
        self.bill.setPlaceholderText(_translate("BillWindow", "Здесь отобразится готовый текст..."))
        self.copy_btn.setText(_translate("BillWindow", "Скопировать в буфер обмена"))
