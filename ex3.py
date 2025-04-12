#Faça um programa que peça um número inteiro e diga se ele é par ou ímpar. 
#Use o operador % (resto da divisão) e uma estrutura condicional. 
# Dica: (num % 2) verifica se a divisão tem resto. Imprima na tela o resultado.


num=int(input('digite um numero para verificarmos se ele é par ou não'))
if(num % 2==0):
    print(f'o numero que digitou {num} é par')
else:
    print(f'o numero {num} não é numero par')