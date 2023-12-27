import sys

from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QPushButton)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 100)
        layout = QHBoxLayout()
        for i in range(1, 4):
            layout.addWidget(QPushButton(f'Кнопка {i}'), i)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
