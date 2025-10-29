class Calculator:
    def __init__(self, op1: float, op2: float):
       self.__op1 = op1
       self.__op2 = op2

    def sum(self):
        return self.__op1 + self.__op2



if __name__ == "__main__":
    calculator = Calculator(1, 2)
    print(calculator.sum())