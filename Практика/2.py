from fractions import Fraction
import sys

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLineEdit,
                             QComboBox,
                             QPushButton)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор дробей')
        self.firstNumerator = QLineEdit()
        self.firstNumerator.setValidator(QIntValidator())
        self.firstDenominator = QLineEdit()
        self.firstDenominator.setValidator(QIntValidator())
        self.operation = QComboBox()
        self.operation.addItems(['+', '-', '*', '/'])
        self.secondNumerator = QLineEdit()
        self.secondNumerator.setValidator(QIntValidator())
        self.secondDenominator = QLineEdit()
        self.secondDenominator.setValidator(QIntValidator())
        self.resultButton = QPushButton('=')
        self.resultButton.clicked.connect(self.solve)
        self.resultNumerator = QLineEdit()
        self.resultNumerator.setReadOnly(True)
        self.resultDenominator = QLineEdit()
        self.resultDenominator.setReadOnly(True)
        horizontalLayout = QHBoxLayout()
        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.firstNumerator)
        verticalLayout.addWidget(self.firstDenominator)
        horizontalLayout.addLayout(verticalLayout)
        horizontalLayout.addWidget(self.operation)
        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.secondNumerator)
        verticalLayout.addWidget(self.secondDenominator)
        horizontalLayout.addLayout(verticalLayout)
        horizontalLayout.addWidget(self.resultButton)
        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.resultNumerator)
        verticalLayout.addWidget(self.resultDenominator)
        horizontalLayout.addLayout(verticalLayout)
        self.setLayout(horizontalLayout)

    def solve(self):
        firstNumerator = int(self.firstNumerator.text())
        firstDenominator = int(self.firstDenominator.text())
        operation = self.operation.currentText()
        secondNumerator = int(self.secondNumerator.text())
        secondDenominator = int(self.secondDenominator.text())
        fraction1 = Fraction(firstNumerator, firstDenominator)
        fraction2 = Fraction(secondNumerator, secondDenominator)
        if operation == '+':
            result = fraction1 + fraction2
        elif operation == '-':
            result = fraction1 - fraction2
        elif operation == '*':
            result = fraction1 * fraction2
        elif operation == '/':
            result = fraction1 / fraction2
        self.resultNumerator.setText(str(result.numerator))
        self.resultDenominator.setText(str(result.denominator))


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
