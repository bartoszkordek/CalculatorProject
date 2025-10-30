'''Calculator module'''


class Calculator:
    '''Calculator class'''
    digits_round = 12

    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        '''Sum two numbers'''
        return self._round(self.__op1 + self.__op2)

    def subtract(self) -> float:
        '''Subtract two numbers'''
        return self._round(self.__op1 - self.__op2)

    def multiply(self) -> float:
        '''Multiply two numbers'''
        return self._round(self.__op1 * self.__op2)

    def divide(self) -> float:
        '''Divide two numbers'''
        if self.__op2 == 0:
            raise ZeroDivisionError("Divisor cannot be 0")
        return self._round(self.__op1 / self.__op2)

    def _round(self, value: float) -> float:
        return round(value, self.digits_round)


def main():
    '''Sample operations'''
    x1 = 1
    x2 = 2

    calculator = Calculator(x1, x2)

    for op, func in [('+', calculator.sum),
                     ('-', calculator.subtract),
                     ('*', calculator.multiply),
                     ('/', calculator.divide)]:
        print(f"{x1} {op} {x2} = {func()}")


if __name__ == "__main__":
    main()
