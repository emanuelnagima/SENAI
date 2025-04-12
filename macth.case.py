num1 = int(input('digite o valor 1:'))
num2 = int(input('digite o valor 2'))
op=input('digite qual operação deseja fazer ')

match op:
    case "+":
        print(f'{num1}+{num2}={num1+num2} ')
    case'-':
        print(f'{num1}-{num2}={num1-num2} ')
    case'*':
        print(f'{num1}*{num2}={num1*num2} ')
    case'/':
        print(f'{num1}/{num2}={num1/num2} ')
    case _:
        print('operação incorreta')