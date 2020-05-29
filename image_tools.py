import PIL
from PIL import Image
from PyQt5.QtWidgets import QFileDialog


# функции для работы с картинками

# изменить размер картинки так, чтобы он уложился в максимум; folder - где сохранить картинку
def resize_picture(picture_path, max_size, folder):
    img = Image.open(picture_path)
    img.thumbnail(max_size, Image.ANTIALIAS)
    path = folder + "." + img.filename.split(".")[-1]
    img.save(path)
    return path


# проверить, выбрана ли картинка для открытия
def is_picture(path):
    file = path.split('/')[-1].lower()
    if file.find('.jpg') != -1 or file.find('.jpeg') != -1 or file.find('.png') != -1 or file.find('.bmp') != -1:
        return True
    else:
        return False


# установить водяной знак
def set_watermark(background_path, watermark_path, position, folder):
    background = Image.open(background_path)
    watermark = Image.open(watermark_path)
    try:
        background.paste(watermark, position, watermark.convert('RGBA'))
    except ValueError:  # There shouldn't be any errors, but in case they will happen...
        print("ValueError exception")
        background.paste(watermark, position)
    path = folder + "." + background.filename.split(".")[-1]
    background.save(path)
    return path


def set_watermark(background, watermark, position):
    try:
        background.paste(watermark, position, watermark.convert('RGBA'))
    except ValueError:  # There shouldn't be any errors, but in case they will happen...
        print("ValueError exception")
        background.paste(watermark, position)
    return background


def save_image(image_path, path):
    img = Image.open(image_path)
    img.save(path)


# изменить размер, чтобы в точности соответствовать заданному
def resize_precision(img_path, new_size, folder):
    image = Image.open(img_path)
    try:
        new_image = image.resize(new_size, PIL.Image.LANCZOS)
    except MemoryError:
        print("output image too big")
        return
    path = folder + "." + image.filename.split(".")[-1]
    new_image.save(path)
    return path


def resize_precision(image, new_size):
    try:
        new_image = image.resize(new_size, PIL.Image.LANCZOS)
        return new_image
    except MemoryError:
        print("output image too big")
        return


def get_file_extension(image):
    return image.filename.split(".")[-1]


def open_picture(self):
    path = select_image(self)
    if path is None:
        return
    if not is_picture(path):
        return
    return path


# открыть диалог с выбором файла
def select_image(parent_window):
    image_format = "Images (*.png *.xpm *.jpg *.jpeg)"
    path = QFileDialog.getOpenFileName(parent_window, "Выберите расположение...", ".", image_format)
    return path[0]


# найти директорию
def select_folder():
    path = QFileDialog.getExistingDirectory()
    return path
