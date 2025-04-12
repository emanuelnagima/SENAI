#Exercício 2 - Faça um programa que peça dois números inteiros e imprima o maior deles. Use apenas uma estrutura condicional. Imprima na tela o resultado.

num1=int(input('digite um numero e veremos qual deles será o maior'))
num2=int(input('digite um numero e veremos qual deles será o maior'))
if(num1 > num2):
    print (f'o numero {num1} é maior que o numero {num2}' )
elif(num1 < num2):
    print(f'o numero {num1} é menor que o numero {num2} ')
else:
    print(f'os valores dos numeros {num1} e {num2} são iguais')