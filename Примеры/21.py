import sys

from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Тест', self)
        self.button.clicked.connect(self.action)

    def action(self):
        self.button.setText('Кнопка нажата')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
