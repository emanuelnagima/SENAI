#Exercício 2 - Faça um programa que peça dois números inteiros e imprima o maior deles. Use apenas uma estrutura

numero1 = int(input('digite um numero para sabermos qual será maior' ))
numero2 = int(input('digite outro para sabermos qual será maior' ))
if(numero1 > numero2):
    print(f'o numero {numero1} é maior que o numero {numero2}')
elif(numero1 < numero2):
    print(f'o numero {numero2} será maior que o numero {numero1}')
else:
    print('os numeros são iguais')