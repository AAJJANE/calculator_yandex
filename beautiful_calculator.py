import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from calc import Ui_Form
from stack import *


class OperationsMixin:
    @staticmethod
    def summ(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def diff(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def mul(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def div(a: float, b: float) -> float:
        return a / b

    @staticmethod
    def pow(a: float, b: float) -> float:
        return a ** b


class Calculator(QMainWindow, Ui_Form, OperationsMixin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table.setDigitCount(10)
        self._stack = Stack()
        self.press_clear()
        self.buttonGroup_digits.buttonClicked.connect(self.press_digit)
        self.btn_dot.clicked.connect(self.press_dot)
        self.btn_clear.clicked.connect(self.press_clear)
        self.btn_plus.clicked.connect(self.press_plus)
        self.btn_minus.clicked.connect(self.press_minus)
        self.btn_mult.clicked.connect(self.press_mul)
        self.btn_div.clicked.connect(self.press_div)
        self.btn_pow.clicked.connect(self.press_pow)
        self.btn_sqrt.clicked.connect(self.press_sqrt)
        self.btn_fact.clicked.connect(self.press_fact)
        self.btn_eq.clicked.connect(self.press_equal)

    def display(self) -> None:
        print(*self._stack.arr)
        self.table.display(str(self._stack))


    def press_digit(self, btn: QPushButton):
        digit = btn.text()
        if not isinstance(self._stack.top, Number):
            self._stack.append(Number())
        self._stack.top.add_digit(digit)
        self.display()

    def press_dot(self):
        ...

    def press_clear(self):
        self._stack.clear()
        self.display()

    def press_plus(self):
        self._stack.append(OperationSum())
        self.display()

    def press_minus(self):
        self._stack.append(OperationMinus())
        self.display()

    def press_mul(self):
        self._stack.append(OperationMul())
        self.display()

    def press_div(self):
        self._stack.append(OperationDiv())
        self.display()

    def press_pow(self):
        self._stack.append(OperationPow())
        self.display()

    def press_sqrt(self):
        self._stack.append(OperationSqrt())
        self._stack.append(MockElement())
        self.press_equal()

    def press_fact(self):
        self._stack.append(OperationFct())
        self._stack.append(MockElement())
        self.press_equal()


    def press_equal(self):
        if len(self._stack) < 3:
            return
        if isinstance(self._stack.arr[-2], Operation):
            a = self._stack.arr[-3].value
            b = self._stack.arr[-1].value
            result = self._stack.arr[-2](a, b)
            self._stack.append(Number(str(result)))
        elif isinstance(self._stack.arr[-3], Operation): # Повтор действия
            a = self._stack.arr.pop().value
            b = self._stack.arr[-1].value
            result = self._stack.arr[-2](a, b)
            self._stack.append(Number(str(result)))
        self.display()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
