import math

class Operation:
    def __init__(self, result = 0, x = 0, y = 0):
        self._result = result
        self.x = x
        self.y = y

    def set_first_number(self):
        print(" ")
        print("Enter the first number: ")
        self.x = float(input())
    def set_second_number(self):
        print("Enter the second number: ")
        self.y = float(input())
    def calculate(self):
        pass
    def get_score(self):
        return self._result
    def get_first_number(self):
        return self.x
    def get_second_number(self):
        return self.y

class Adding(Operation):
    def calculate(self):
        self.set_second_number(self)
        self._result = self.x + self.y
        print("= ",self.get_score(self))
    def set_second_number(self):
        print("Enter the second number: ")
        print(self.get_first_number(self), " + ", end=" ")
        self.y = float(input())

class Subtract(Operation):
    def calculate(self):
        self.set_second_number(self)
        self._result = self.x - self.y
        print("= ", self.get_score(self))
    def set_second_number(self):
        print("Enter the second number: ")
        print(self.get_first_number(self), " - ", end=" ")
        self.y = float(input())

class Multiplication(Operation):
    def calculate(self):
        self.set_second_number(self)
        self._result = self.x * self.y
        print("= ", self.get_score(self))
    def set_second_number(self):
        print("Enter the second number: ")
        print(self.get_first_number(self), " * ", end=" ")
        self.y = float(input())

class Division(Operation):
    def calculate(self):
        self.set_second_number(self)
        if self.y != 0:
            self._result = self.x / self.y
            print("= ", self.get_score(self))
        else:
            print("Dividing by zero is impossible.")
    def set_second_number(self):
        print("Enter the second number: ")
        print(self.get_first_number(self), " / ", end=" ")
        self.y = float(input())

class Square(Operation):
    def calculate(self):
        if self.x > 0:
            self._result = math.sqrt(self.x)
            print("The square root of ", Ascii, self.x, "= ", self.get_score(self))
        else:
            print("Error.")

if __name__ == "__main__":
    print("Hello world")
    while (True):
        A = Operation
        A.set_first_number(A)
        print("Choose action by typing it's number: ")
        print("1. Add.")
        print("2. Subtract.")
        print("3. Multiply.")
        print("4. Divide.")
        print("5. Square.")
        print("6. Exit.")
        a = int(input())
        if a == 1:
            A = Adding
            A.calculate(A)
        elif a  == 2:
            A = Subtract
            A.calculate(A)
        elif a == 3:
            A = Multiplication
            A.calculate(A)
        elif a == 4:
            A = Division
            A.calculate(A)
        elif a == 5:
            A = Square
            A.calculate(A)
        elif a == 6:
            break
        else:
            pass






