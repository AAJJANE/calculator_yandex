from math import factorial


class Stack:
    def __init__(self):
        self.arr: list[Element] = [Number()]

    def clear(self) -> None:
        self.arr = [Number()]

    def __str__(self) -> str:
        for el in reversed(self.arr):
            if isinstance(el, Number):
                return str(el)

    @property
    def top(self) -> 'Element':
        return self.arr[-1]

    def append(self, el: 'Element') -> None:
        if isinstance(el, Operation) and isinstance(self.top, Operation):
            self.arr.pop()
        self.arr.append(el)

    def __len__(self) -> int:
        return len(self.arr)


class Element:
    ...



class Number(Element):
    def __init__(self, value: str='0'):
        self._value = value

    def __str__(self) -> str:
        v = round(float(self._value), 6)
        return str(v).removesuffix('.0')

    def add_digit(self, digit: str) -> None:
        if self._value == '0':
            self._value = digit
        else:
            self._value += digit

    @property
    def value(self) -> float:
        return float(self._value)


class MockElement(Element):
    def __str__(self) -> str:
        return '_'

    @property
    def value(self) -> float:
        return None


class Operation(Element):
    ...


class UnaryOperation(Operation):
    pass


class BinaryOperation(Operation):
    pass


class OperationSum(BinaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return a + b

    def __str__(self) -> str:
        return '+'


class OperationMinus(BinaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return a - b

    def __str__(self) -> str:
        return '-'


class OperationMul(BinaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return a * b

    def __str__(self) -> str:
        return '*'


class OperationDiv(BinaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return a / b

    def __str__(self) -> str:
        return '/'


class OperationPow(BinaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return a ** b

    def __str__(self) -> str:
        return '^'


class OperationSqrt(UnaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return a ** 0.5

    def __str__(self) -> str:
        return 'sqrt'


class OperationFct(UnaryOperation):
    def __call__(self, a: float, b: float) -> float:
        return factorial(int(a))

    def __str__(self) -> str:
        return 'sqrt'