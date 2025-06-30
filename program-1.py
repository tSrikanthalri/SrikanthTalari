class Calculator:
    def __init__(self,num1,num2,operation):
        self.num1 = float(num1)
        self.num2 = float(num2)
        self.operation = operation


    def calculate(self):
        if self.operation == "add":
            return self.num1 + self.num2
        
        elif self.operation == "subtract":
            return self.num1 - self.num2
        
        elif self.operation == "multiply":
            return self.num1 * self.num2
        
        elif self.operation == "divide":
            return self.num1 / self.num2
        else:
            return "invalid operation"

num1 = input("enter the number1: ")
num2 = input("enter the number2: ")
operation = input("Enter the add/subtract/multiply/divide: ")


calc = Calculator(num1,num2,operation)
result = calc.calculate()
print("Result:",result)
                 
        
        
