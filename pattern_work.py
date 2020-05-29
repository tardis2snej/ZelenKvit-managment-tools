from PyQt5.QtWidgets import QMessageBox, QFileDialog


# функции для работы с шаблонами текстов

# проверяет, содержит ли текст необходимые метки (требуемые поля)
def verify_pattern(self, pattern, required_fields, message="Возможно, шаблон составлен неправильно."):
    for field in required_fields:
        if field not in pattern:
            QMessageBox.critical(self, "Шаблон не распознан", message, QMessageBox.Ok)
            return False
    return True


# загрузить шаблон из файла
def load_pattern(self, path, message="Не найден файл с шаблоном.\n"
                                     "Выберите расположение..."):
    try:
        file = open(path, 'r', encoding='utf8')
    except FileNotFoundError:
        QMessageBox.critical(self, "Ошибка", message, QMessageBox.Open)
        path = QFileDialog.getOpenFileName(self, "Выберите расположение шаблона...", ".", "Text (*.txt)")[0]
        if path == '':
            return None
        file = open(path, 'r', encoding='utf8')
    pattern = file.read()
    return pattern
