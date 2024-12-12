import sys
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QFontDialog, \
    QColorDialog, QStatusBar, QToolBar


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация
        self.setWindowTitle('t')
        self.setWindowIcon(QIcon('icon.png'))  # Путь к иконке окна
        self.setGeometry(100, 100, 800, 600)

        # Текстовое поле для редактирования
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Статус-бар
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Меню
        self.create_menu()

        # Панель инструментов
        self.create_toolbar()

    def create_menu(self):
        # Создаем меню
        menu_bar = self.menuBar()

        # Файл
        file_menu = menu_bar.addMenu('Файл')

        new_action = QAction(QIcon('new_icon.png'), 'Новый', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)

        open_action = QAction(QIcon('open_icon.png'), 'Открыть', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)

        save_action = QAction(QIcon('save_icon.png'), 'Сохранить', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Редактирование
        edit_menu = menu_bar.addMenu('Редактирование')

        font_action = QAction('Изменить шрифт', self)
        font_action.triggered.connect(self.change_font)

        bgcolor_action = QAction('Изменить фон', self)
        bgcolor_action.triggered.connect(self.change_background_color)

        edit_menu.addAction(font_action)
        edit_menu.addAction(bgcolor_action)

    def create_toolbar(self):
        # Создаем панель инструментов
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        # Добавляем кнопки на панель
        new_action = QAction(QIcon('new_icon.png'), 'Новый', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)

        open_action = QAction(QIcon('open_icon.png'), 'Открыть', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        save_action = QAction(QIcon('save_icon.png'), 'Сохранить', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

        font_action = QAction('Шрифт', self)
        font_action.triggered.connect(self.change_font)
        toolbar.addAction(font_action)

        bgcolor_action = QAction('Цвет фона', self)
        bgcolor_action.triggered.connect(self.change_background_color)
        toolbar.addAction(bgcolor_action)

    def new_file(self):
        self.text_edit.clear()
        self.statusbar.showMessage('Новый файл создан')

    def open_file(self):
        # Используем правильный способ для получения опций
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)', options=QFileDialog.Options())
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.text_edit.setText(file.read())
            self.statusbar.showMessage(f'Открыт файл: {file_name}')

    def save_file(self):
        # Используем правильный способ для получения опций
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)', options=QFileDialog.Options())
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
            self.statusbar.showMessage(f'Файл сохранен: {file_name}')

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

    def change_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setStyleSheet(f'background-color: {color.name()};')
            self.statusbar.showMessage(f'Фон изменен на {color.name()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Путь к иконкам для действий, например: 'icons/new_icon.png', 'icons/open_icon.png'
    editor = TextEditor()
    editor.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    app = QApplication(sys.argv)


    editor = TextEditor()
    editor.show()

    sys.exit(app.exec())
