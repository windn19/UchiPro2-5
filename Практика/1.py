import sys

from PyQt6.QtWidgets import (QWidget,
                             QFormLayout,
                             QLineEdit,
                             QApplication,
                             QVBoxLayout,
                             QPushButton,
                             QHBoxLayout,
                             QDateEdit)


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация')
        nameField = QLineEdit()
        passwordField = QLineEdit()
        dateField = QDateEdit()
        buttonReg = QPushButton('Зарегистрироваться')
        nameField.setMaxLength(10)
        passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        verticalLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Имя', nameField)
        formLayout.addRow('Пароль', passwordField)
        formLayout.addRow('Дата рождения', dateField)
        verticalLayout.addLayout(formLayout)
        verticalLayout.addWidget(buttonReg)
        self.setLayout(verticalLayout)


class Authorisation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        nameField = QLineEdit()
        passwordField = QLineEdit()
        buttonLogin = QPushButton('Войти')
        buttonReg = QPushButton('Регистрация')
        buttonReg.clicked.connect(self.registration)
        nameField.setMaxLength(10)
        passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        verticalLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Имя', nameField)
        formLayout.addRow('Пароль', passwordField)
        verticalLayout.addLayout(formLayout)
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(buttonLogin)
        horizontalLayout.addWidget(buttonReg)
        verticalLayout.addLayout(horizontalLayout)
        self.setLayout(verticalLayout)

    def registration(self):
        self.reg = Registration()
        self.reg.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = Authorisation()
    auth.show()
    sys.exit(app.exec())
