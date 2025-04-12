nome=str(input('Olá, digite seu nome para realizarmos uma pesquisa'))
idade=int(input(f'{nome}insira sua idade para sabermos se vc ja pode votar!'))
if(idade >= 18):
    print('Vc é obrigado a votar')
elif(idade >= 16):
    print('É opcional vc votar')
else:
    print('Vc não pode votar')
print('pesquisa encerrada, obrigado')

#-----------------------------------------------------------------------------------
#exercicio do professor
nome1=str(input('Olá, digite seu nome para realizarmos uma pesquisa'))
idade1=int(input(f'{nome1}insira sua idade para sabermos se vc ja pode votar!'))

if(idade1 < 16 ):
    print('Vc não pode votar')
elif(idade1 >= 16) and (idade1 <= 17):
    print('É opcional vc votar')
else:
    print('Vc é obrigado a votar')
print('pesquisa encerrada, obrigado')


