import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример заголовка')
        self.resize(300, 200)
        self.move(100, 100)
        button = QPushButton('Кнопка', parent=self)
        button.resize(10, 50)
        button.move(100, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
