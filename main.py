from src.Calculator import Calculator

replay = 'y'
while replay == 'y':
    newCount = Calculator()
    newCount.getResult()
    replay = input('restart? (y / n)')