import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import image_tools
from UI import image_processing as design
from ProcessingImage import ProcessingImage


# окно для работы с картинками
class ProcessImageWindow(QtWidgets.QMainWindow, design.Ui_image_processing):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # переменные
        self.preview_image_path = "preview.jpg"  # Default preview image
        self.working_image = ProcessingImage(self.preview_image_path)
        self.working_image_path = "temp\picture.jpg"

        self.watermark_position = (0, 0)
        self.watermark_scale = 1

        self.photo_group = []  # фотографии, к которым мы применим эффекты

        self.first_frame = True  # флаг для идентификации первого "кадра" окна

        self.manual_mode = False

        self.working_image.update_processing_image()
        w, h = self.working_image.current_image.size
        self.orig_size.setText(str(w) + "x" + str(h) + "px")
        self.curr_size.setText(str(w) + "x" + str(h) + "px")
        self.set_picturebox(self.preview_image_path)  # установка картинки предпросмотра по умолчанию

        self.set_event_listeners()

    # установка слушателей на все кнопки
    def set_event_listeners(self):
        self.open_preview.clicked.connect(self.open_single_picture_for_editing)
        self.open_watermark_button.clicked.connect(self.open_watermark)
        self.watermark_position_x.valueChanged.connect(self.watermark_position_changed)
        self.watermark_position_y.valueChanged.connect(self.watermark_position_changed)
        self.watermark_scale_spinbox.valueChanged.connect(self.watermark_scale_changed)
        self.save_preview.clicked.connect(self.save_single_image)
        self.delete_watermark_button.clicked.connect(self.delete_watermark)
        self.main_img_scale_spinbox.valueChanged.connect(self.main_img_scale_changed)
        self.select_filegroup.clicked.connect(self.select_photo_group)
        self.save_filegroup.clicked.connect(self.apply_to_photo_group)
        self.update_button.clicked.connect(self.updates)
        self.manual_update_mode_checkBox.clicked.connect(self.change_manual_mode)

    # изменение режима обновления
    def change_manual_mode(self):
        self.manual_mode = not self.manual_mode
        if not self.manual_mode:
            self.updates()

    # установка картинки предпросмотра
    def set_preview(self, picture):
        # получить максимальный размер контейнера
        max_size = self.left_groupbox.size()
        max_width = max_size.width()
        max_height = max_size.height()

        self.preview_image_path = picture
        preview_image = image_tools.resize_picture(self.preview_image_path, (max_width, max_height),
                                                   "temp/preview")  # Resize image
        self.set_picturebox(preview_image)

    # установить картинку в picturebox
    def set_picturebox(self, preview_image):
        pixmap = QPixmap(preview_image)
        self.picture_label.setPixmap(pixmap)

    # сделать, чтобы превью помещалось в окно, когда изменяется размер картинки
    def resizeEvent(self, *args):
        if self.first_frame:
            self.first_frame = False
            return
        self.set_preview(self.preview_image_path)

    # открыть одну картинку для работы
    def open_single_picture_for_editing(self):
        path = image_tools.open_picture(self)
        if path == "" or path is None:
            return
        self.working_image = ProcessingImage(path)
        w, h = self.working_image.current_image.size
        self.orig_size.setText(str(w) + "x" + str(h) + "px")
        self.working_image_path = "temp/processing." + image_tools.get_file_extension(self.working_image.current_image)
        self.updates()

    # открыть водяной знак для наложения
    def open_watermark(self):
        path = image_tools.open_picture(self)
        if path is None:
            return
        self.working_image.set_watermark(path, self.watermark_position, self.watermark_scale)
        self.watermark_path_label.setText(path)
        self.updates()

    # получить параметры позиции и подвинуть водяной знак
    def watermark_position_changed(self):
        self.watermark_position = (int(self.watermark_position_x.text()), int(self.watermark_position_y.text()))
        if self.working_image.watermark is None:
            return
        self.working_image.watermark.image_position = self.watermark_position
        if not self.manual_mode:
            self.updates()

    # получить новый размер и изменить водяной знак
    def watermark_scale_changed(self):
        self.watermark_scale = int(self.watermark_scale_spinbox.text()) / 100
        if self.working_image.watermark is None:
            return
        self.working_image.watermark.image_scale = self.watermark_scale
        if not self.manual_mode:
            self.updates()

    # сохранить текущую картинку с превью
    def save_single_image(self):
        path = QFileDialog.getSaveFileName(self, "Сохранить...", "file", "Images (*.png *.xpm *.jpg *.jpeg)")
        if path[0] == '':
            return
        self.working_image.save_final_image(path[0])

    # удалить водяной знак с текущей картинки
    def delete_watermark(self):
        self.working_image.watermark = None
        self.reset_displayed_watermark_settings()
        self.updates()

    def reset_displayed_watermark_settings(self):
        self.watermark_path_label.setText("")
        self.watermark_scale_spinbox.setValue(100)
        self.watermark_scale = 1

    # обновить размер главной картинки
    def main_img_scale_changed(self):
        new_scale = int(self.main_img_scale_spinbox.text()) / 100
        self.working_image.image_scale = new_scale
        new_size = (int(self.working_image.original_size[0] * new_scale), int(self.working_image.original_size[1] * new_scale))
        self.curr_size.setText(str(new_size[0]) + "x" + str(new_size[1]) + "px")
        if not self.manual_mode:
            self.updates()

    # выбрать группу фотографий, на которые нужно применить эффект
    def select_photo_group(self):
        input_path = image_tools.select_folder()
        if input_path == "":
            return
        input_path += "/"
        self.photo_group = []
        self.input_filegroup_path.setText(input_path)

        allfiles = os.listdir(input_path)
        for file in allfiles:
            if image_tools.is_picture(input_path + file):
                self.photo_group.append(input_path + file)
        print(self.photo_group)

    # применить изменения к группе фотографий
    def apply_to_photo_group(self):
        output_path = image_tools.select_folder()
        if output_path == "" or not self.photo_group:
            return
        output_path += "/"
        self.updates()
        orig_copy = self.working_image.get_copy()
        counter = 1
        for photo_path in self.photo_group:
            orig_copy.set_orig_picture(photo_path)
            filename = "photo" + str(counter)
            orig_copy.save_final_image(output_path + filename + "." + image_tools.get_file_extension(orig_copy.current_image))
            counter += 1

    def updates(self):
        # print("upd")
        self.working_image.save_final_image(self.working_image_path)
        self.set_preview(self.working_image_path)
