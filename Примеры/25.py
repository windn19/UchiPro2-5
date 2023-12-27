import sys

from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QLineEdit)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 100)
        password = QLineEdit(parent=self)
        password.setPlaceholderText('Введите пароль')
        password.setClearButtonEnabled(True)
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setMaxLength(6)
        password.move(30, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
