import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, \
    QFontDialog
from PyQt6.QtGui import QIcon, QAction


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простой текстовый редактор")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.create_toolbar()

        # Создание меню
        self.create_menu()

    def create_toolbar(self):
        # Панель инструментов
        toolbar = self.addToolBar("Основная панель")

        # Добавляем кнопки на панель
        open_action = QAction(QIcon("open.png"), "Открыть", self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        save_action = QAction(QIcon("save.png"), "Сохранить", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

        copy_action = QAction(QIcon("copy.png"), "Копировать", self)
        copy_action.triggered.connect(self.copy_text)
        toolbar.addAction(copy_action)

        cut_action = QAction(QIcon("cut.png"), "Вырезать", self)
        cut_action.triggered.connect(self.cut_text)
        toolbar.addAction(cut_action)

        paste_action = QAction(QIcon("paste.png"), "Вставить", self)
        paste_action.triggered.connect(self.paste_text)
        toolbar.addAction(paste_action)

        font_action = QAction(QIcon("font.png"), "Изменить шрифт", self)
        font_action.triggered.connect(self.change_font)
        toolbar.addAction(font_action)



    def create_menu(self):
        # Создаем меню
        menubar = self.menuBar()

        # Меню "Файл"
        file_menu = menubar.addMenu("Файл")

        open_action = QAction("Открыть", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Сохранить", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Меню "Правка"
        edit_menu = menubar.addMenu("Правка")

        copy_action = QAction("Копировать", self)
        copy_action.triggered.connect(self.copy_text)
        edit_menu.addAction(copy_action)

        cut_action = QAction("Вырезать", self)
        cut_action.triggered.connect(self.cut_text)
        edit_menu.addAction(cut_action)

        paste_action = QAction("Вставить", self)
        paste_action.triggered.connect(self.paste_text)
        edit_menu.addAction(paste_action)

        # Меню "Шрифт"
        font_menu = menubar.addMenu("Шрифт")

        change_font_action = QAction("Изменить шрифт", self)
        change_font_action.triggered.connect(self.change_font)
        font_menu.addAction(change_font_action)

    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                self.text_edit.setText(f.read())

    def save_file(self):
        file, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(self.text_edit.toPlainText())

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_edit.textCursor().selectedText())

    def cut_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_edit.textCursor().selectedText())
        self.text_edit.textCursor().removeSelectedText()

    def paste_text(self):
        clipboard = QApplication.clipboard()
        self.text_edit.textCursor().insertText(clipboard.text())

    def change_font(self):
        font, ok = QFontDialog.getFont(self.text_edit.font(), self)
        if ok:
            self.text_edit.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec())
