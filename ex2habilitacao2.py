
nome = str(input('Olá, digite seu nome para realizarmos uma pesquisa: '))
idade = int(input(f'{nome}, insira sua idade para sabermos se vc ja tirar habilitação! '))
if (idade <= 17):
    print('Vc ainda não pode tirar carta')
elif (idade >= 18):
    print('Parabéns, vc pode tirar carta')
    resposta = input('vc ja possui habilitação? ')
    if (resposta == "sim"):
        print('Parabéns, voce pode dirigir!')
        tipoHabilitacao = str(input('qual sua categoria, A, B, C ou D? '))
        tipoHabilitacao = tipoHabilitacao.lower()
        if (tipoHabilitacao == "a"):
            print('Vc tem carteira de moto')
        elif (tipoHabilitacao == "b"):
            print('vc tem carteira de carro')
        elif (tipoHabilitacao == "AB"):
            print('vc tem habilitação de carro e moto')
        
