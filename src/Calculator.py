class Calculator:
    
    def __init__(self) -> None:
        self.num1 = int(input('Digite o primeiro número: '))
        self.num2 = int(input('Digite o segundo número: '))
        self.operator = input('Escolha o operador desejado(+ - / *)')

    def sum(self):
        return (self.num1 + self.num2)

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2

    def getResult(self):
        if(self.operator == "+"):
            print(self.sum())

        elif(self.operator == "-"):
            print(self.subtraction())

        elif(self.operator == "/"):
            print(self.division())
            
        elif(self.operator == "*"):
            print(self.multiplication())


