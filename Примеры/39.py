import sys

from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QGridLayout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        for i in range(1, 4):
            for j in range(1, 3):
                layout.addWidget(QPushButton(f'Кнопка {i} {j}'), i, j)
        layout.addWidget(QPushButton(f'Кнопка 4 3'), 4, 3)
        layout.addWidget(QPushButton(f'Кнопка'), 5, 1, 5, 3)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
