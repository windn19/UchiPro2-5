import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QFormLayout, QPushButton,
                             QLineEdit, QComboBox, QDateEdit)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        name = QLineEdit()
        gender = QComboBox()
        date = QDateEdit()
        gender.addItems(['муж', 'жен'])
        button = QPushButton('Отправить')
        layout.addRow('Имя', name)
        layout.addRow('Пол', gender)
        layout.addRow('Дата рождения', date)
        layout.addWidget(button)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
