from PIL import Image
import image_tools


# класс для работы с картинкой, которая обрабатывается
class ProcessingImage:
    def __init__(self, base_image, scale=1, position=(0, 0)):
        self.orig_img_path = None
        self.current_image = None
        self.original_size = (0, 0)
        self.set_orig_picture(base_image)

        self.image_scale = scale
        self.image_position = position
        self.watermark = None  # ProseccingImage(watermark_path)

    def set_orig_picture(self, path):
        self.orig_img_path = path
        # if self.orig_img_path is None or self.orig_img_path == "":
        #     self.current_image
        try:
            self.current_image = Image.open(path)
        except FileNotFoundError:
            self.current_image = Image.new('1', (1, 1))
            self.orig_img_path = "temp/picture.jpg"
            self.current_image.save(self.orig_img_path)
        self.original_size = self.current_image.size

    # коставить водяной знак
    def set_watermark(self, path, position, scale):
        self.watermark = ProcessingImage(path, scale, position)

    # изменить размер главной картинки
    def scale_main_image(self):
        width, height = self.current_image.size
        new_size = (int(width * self.image_scale), int(height * self.image_scale))
        self.current_image = image_tools.resize_precision(self.current_image, new_size)

    # поставить водяной знак на картинку
    def apply_watermark(self):
        if self.watermark is None:
            return
        self.current_image = image_tools.set_watermark(self.current_image, self.watermark.current_image,
                                                       self.watermark.image_position)

    # пересчитать все наложенные эффекты. После этого self.current_image представляет конечную готовую картинку
    def update_processing_image(self):
        # начинаем с самого начала
        self.current_image = Image.open(self.orig_img_path)
        # все изменения размера главной картинки
        self.scale_main_image()
        # если есть водяной знак
        if self.watermark is not None:
            self.watermark.update_processing_image()
            self.apply_watermark()

    # сохранить в path
    def save_final_image(self, path):
        self.update_processing_image()
        self.current_image.save(path)

    def get_copy(self):
        copy = ProcessingImage(self.orig_img_path, self.image_scale, self.image_position)
        if self.watermark is not None:
            copy.watermark = self.watermark.get_copy()
        return copy
