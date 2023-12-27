import sys

from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QPushButton)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        verticalLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        for i in range(1, 3):
            horizontalLayout.addWidget(QPushButton(f'Кнопка {i}'))
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout = QHBoxLayout()
        for i in range(1, 4):
            horizontalLayout.addWidget(QPushButton(f'Кнопка {i}'))
        verticalLayout.addLayout(horizontalLayout)
        self.setLayout(verticalLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
