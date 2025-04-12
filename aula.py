#if, else, e elif: condições se forem verdadeiras ou não
#em python não temos a estrtura de { }


numero1 = 1 
numero2 = 10

if (numero1 > numero2):
    print(f'o valor {numero1} é maior que {numero2}')
    print('se')
    print("-------------------------------------------")
elif(numero2 > numero1):
    print(f'o valor {numero2} é maior que {numero1}')
    print('se não')
    print("-------------------------------------------")
print('acabou o meu if')

numeroo1 = 10 
numeroo2 = 10

if (numeroo1 > numeroo2):
    print(f'o valor {numeroo1} é maior que {numeroo2}')
    print('se')
    print("-------------------------------------------")
elif(numeroo2 > numeroo1):
    print(f'o valor {numeroo2} é maior que {numeroo1}')
    print('se não')
    print("-------------------------------------------")
else:
    print(f'o valor de {numeroo1} é igual ao de {numeroo2}')
    print('iguail')
print('acabou o meu if')

#---------------------------------------------------------------------------------------
nu1=int(input('digite um numero'))
nu2=int(input('digite outro numero'))
if (nu1 > nu2):
    print(f'o valor {nu1} é maior que {nu2}')
    print('se')
    print("-------------------------------------------")
elif(nu2 > nu1):
    print(f'o valor {nu1} é maior que {nu2}')
    print('se não')
    print("-------------------------------------------")
else:
    print(f'o valor de {nu1} é igual ao de {nu2}')
    print('igual')
print('acabou o meu if')

