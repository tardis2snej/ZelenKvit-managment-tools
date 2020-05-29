# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_order_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddOrder(object):
    def setupUi(self, AddOrder):
        AddOrder.setObjectName("AddOrder")
        AddOrder.resize(1087, 885)
        AddOrder.setStyleSheet("font: 12pt \"Garamond\";")
        self.centralwidget = QtWidgets.QWidget(AddOrder)
        self.centralwidget.setStyleSheet("#centralwidget { \n"
"    background-color: qlineargradient(spread:pad, x1:0.084, y1:0.329545, x2:0.901, y2:0.551136, stop:0 rgba(221, 255, 199, 255), stop:0.232451 rgba(187, 255, 184, 255), stop:0.680092 rgba(221, 255, 164, 255), stop:1 rgba(145, 255, 161, 255)); \n"
"}\n"
"#add_to_archive_btn, #copy_to_clipboard_btn {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(114, 201, 113, 137), stop:0.264151 rgba(116, 234, 105, 211), stop:0.496115 rgba(188, 224, 133, 124), stop:0.778024 rgba(163, 228, 112, 220), stop:1 rgba(214, 255, 152, 182));}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.money_transferred_fld = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.money_transferred_fld.setMaximum(99999999.99)
        self.money_transferred_fld.setObjectName("money_transferred_fld")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.money_transferred_fld)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pay_date_fld = QtWidgets.QDateTimeEdit(self.groupBox)
        self.pay_date_fld.setObjectName("pay_date_fld")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pay_date_fld)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.city_fld = QtWidgets.QLineEdit(self.groupBox)
        self.city_fld.setObjectName("city_fld")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.city_fld)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.post_num_fld = QtWidgets.QLineEdit(self.groupBox)
        self.post_num_fld.setObjectName("post_num_fld")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.post_num_fld)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.client_name_fld = QtWidgets.QLineEdit(self.groupBox)
        self.client_name_fld.setObjectName("client_name_fld")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.client_name_fld)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.telephone_fld = QtWidgets.QLineEdit(self.groupBox)
        self.telephone_fld.setObjectName("telephone_fld")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.telephone_fld)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.add_pos_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_pos_btn.setObjectName("add_pos_btn")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.add_pos_btn)
        self.scroll_orders = QtWidgets.QScrollArea(self.groupBox)
        self.scroll_orders.setWidgetResizable(True)
        self.scroll_orders.setObjectName("scroll_orders")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 85))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scroll_orders.setWidget(self.scrollAreaWidgetContents)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.scroll_orders)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.order_num_fld = QtWidgets.QSpinBox(self.groupBox)
        self.order_num_fld.setMaximum(10000000)
        self.order_num_fld.setObjectName("order_num_fld")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.order_num_fld)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.where_from_short_fld = QtWidgets.QLineEdit(self.groupBox_2)
        self.where_from_short_fld.setObjectName("where_from_short_fld")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.where_from_short_fld)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.povider_price_fld = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.povider_price_fld.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.povider_price_fld.setSuffix("")
        self.povider_price_fld.setMaximum(99999999.99)
        self.povider_price_fld.setObjectName("povider_price_fld")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.povider_price_fld)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.selling_price_fld = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.selling_price_fld.setSuffix("")
        self.selling_price_fld.setMaximum(99999999.99)
        self.selling_price_fld.setObjectName("selling_price_fld")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.selling_price_fld)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.more_contacts_fld = QtWidgets.QLineEdit(self.groupBox_2)
        self.more_contacts_fld.setObjectName("more_contacts_fld")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.more_contacts_fld)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.notes_fld = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.notes_fld.setObjectName("notes_fld")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.notes_fld)
        self.viber_group_fld = QtWidgets.QComboBox(self.groupBox_2)
        self.viber_group_fld.setObjectName("viber_group_fld")
        self.viber_group_fld.addItem("")
        self.viber_group_fld.setItemText(0, "")
        self.viber_group_fld.addItem("")
        self.viber_group_fld.addItem("")
        self.viber_group_fld.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.viber_group_fld)
        self.provider_discount_fld = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.provider_discount_fld.setSuffix("")
        self.provider_discount_fld.setMaximum(99.99)
        self.provider_discount_fld.setObjectName("provider_discount_fld")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.provider_discount_fld)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.generate_order_btn = QtWidgets.QCommandLinkButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_order_btn.sizePolicy().hasHeightForWidth())
        self.generate_order_btn.setSizePolicy(sizePolicy)
        self.generate_order_btn.setObjectName("generate_order_btn")
        self.verticalLayout_2.addWidget(self.generate_order_btn)
        self.generated_text_area = QtWidgets.QTextBrowser(self.frame_2)
        self.generated_text_area.setEnabled(False)
        self.generated_text_area.setReadOnly(False)
        self.generated_text_area.setObjectName("generated_text_area")
        self.verticalLayout_2.addWidget(self.generated_text_area)
        self.copy_to_clipboard_btn = QtWidgets.QPushButton(self.frame_2)
        self.copy_to_clipboard_btn.setObjectName("copy_to_clipboard_btn")
        self.verticalLayout_2.addWidget(self.copy_to_clipboard_btn)
        self.add_to_archive_btn = QtWidgets.QPushButton(self.frame_2)
        self.add_to_archive_btn.setObjectName("add_to_archive_btn")
        self.verticalLayout_2.addWidget(self.add_to_archive_btn)
        self.horizontalLayout.addWidget(self.frame_2)
        AddOrder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddOrder)
        self.statusbar.setObjectName("statusbar")
        AddOrder.setStatusBar(self.statusbar)

        self.retranslateUi(AddOrder)
        QtCore.QMetaObject.connectSlotsByName(AddOrder)

    def retranslateUi(self, AddOrder):
        _translate = QtCore.QCoreApplication.translate
        AddOrder.setWindowTitle(_translate("AddOrder", "Добавить заказ"))
        self.groupBox.setTitle(_translate("AddOrder", "Обязательная информация"))
        self.label.setText(_translate("AddOrder", "Денег перечислено:"))
        self.label_2.setText(_translate("AddOrder", "Дата:"))
        self.label_3.setText(_translate("AddOrder", "Адрес:"))
        self.label_4.setText(_translate("AddOrder", "Город:"))
        self.label_5.setText(_translate("AddOrder", "Номер отделения:"))
        self.label_6.setText(_translate("AddOrder", "ФИО получателя:"))
        self.label_7.setText(_translate("AddOrder", "Тел. номер получателя:"))
        self.label_8.setText(_translate("AddOrder", "Заказы - каждый в новом поле:"))
        self.add_pos_btn.setText(_translate("AddOrder", "Добавить позицию..."))
        self.label_16.setText(_translate("AddOrder", "Номер заказа:"))
        self.groupBox_2.setTitle(_translate("AddOrder", "Дополнительная информация"))
        self.label_9.setText(_translate("AddOrder", "Откуда пришли:"))
        self.label_10.setText(_translate("AddOrder", "Группа в Viber:"))
        self.label_11.setText(_translate("AddOrder", "Розница поставщика:"))
        self.povider_price_fld.setSpecialValueText(_translate("AddOrder", "0"))
        self.label_12.setText(_translate("AddOrder", "Скидка поставщика (%):"))
        self.label_13.setText(_translate("AddOrder", "Розница ЗеленКвіт:"))
        self.label_14.setText(_translate("AddOrder", "Доп. контакты:"))
        self.label_15.setText(_translate("AddOrder", "Примечания:"))
        self.viber_group_fld.setItemText(1, _translate("AddOrder", "Есть"))
        self.viber_group_fld.setItemText(2, _translate("AddOrder", "Нет"))
        self.viber_group_fld.setItemText(3, _translate("AddOrder", "Не надо"))
        self.provider_discount_fld.setSpecialValueText(_translate("AddOrder", "15"))
        self.generate_order_btn.setText(_translate("AddOrder", "Сгенерировать форму заказа"))
        self.generated_text_area.setHtml(_translate("AddOrder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Garamond\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Здесь отобразится сгенерированный текст...</p></body></html>"))
        self.copy_to_clipboard_btn.setText(_translate("AddOrder", "Скопировать в буфер обмена"))
        self.add_to_archive_btn.setText(_translate("AddOrder", "Добавить данные в архив"))