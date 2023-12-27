import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QGridLayout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Номеронабиратель')
        layout = QGridLayout()
        buttons = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]
        for i in range(4):
            for j in range(3):
                button = QPushButton(buttons[i][j])
                button.setFixedSize(100, 100)
                button.setFont(QFont('Times', 20))
                layout.addWidget(button, i, j)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)
        self.setLayout(layout)
        self.char = 'X'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
