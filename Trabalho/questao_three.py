

dig = 1.10
ico = 1.00
ipb = 0.40
fot = 0.20
encs = 15.00
encd = 40.00

print('Bem-Vindo a Loja de Gelados do Talles Robert')

valor = 0


def escolha_servico():

    while True:
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>>>')
        servicoM = servico.upper()

        if not servicoM == 'DIG' and not servicoM == "ICO" and not servicoM == "IPB" and not servicoM == 'FOT':
            print('Escolha inválida, entre com o tipo do serviço novamente')
            print('')

        elif servicoM == 'DIG':
            return dig

        elif servicoM == "ICO":
            return ico

        elif servicoM == "IPB":
            return ipb

        elif servicoM == "FOT":
            return fot


def num_pagina():
    paginas = input('Entre com o número de paginas: ')
    if paginas < 20:
        return paginas
    elif paginas >= 20 and paginas < 200:
        desconto = paginas * 0.15
        return paginas, desconto
    elif paginas >= 200 and paginas < 2000:
        desconto = paginas * 0.20
        return paginas, desconto
    elif paginas >= 2000 and paginas < 20000:
        desconto = paginas * 0.25
        return paginas, desconto
    elif paginas >= 20000:
        return print('Não é aceito pedidos nessa quantidade de páginas.')
    
teste = escolha_servico
teste2 = num_pagina

print(f'{teste} e {teste2}')

 