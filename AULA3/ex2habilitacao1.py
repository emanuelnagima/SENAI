nome=str(input('Olá, digite seu nome para realizarmos uma pesquisa'))
idade=int(input(f'{nome} insira sua idade para sabermos se vc ja tirar habilitação!'))
if (idade >= 18):
    print('vc ja pode tirar a carta')
elif (idade < 18):
    print('infelizmente vc não pode tirar a carta ainda!')
