

dig = 1.10
ico = 1.00
ipb = 0.40
fot = 0.20
encs = 15.00
encd = 40.00

print('Bem-Vindo a Loja de Gelados do Talles Robert')


def escolha_servico():

    while True:
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servicoM = input('>>>').upper()

        if servicoM not in ['DIG', "ICO", "IPB", 'FOT']:
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
    while True:
        try:
            paginas = int(input('Entre com o número de paginas: '))
            if paginas < 20:
                return paginas
                break
            elif paginas >= 20 and paginas < 200:
                desconto = paginas - (paginas * 0.15)
                return desconto
                break
            elif paginas >= 200 and paginas < 2000:
                desconto = paginas - (paginas * 0.20)
                return desconto
                break
            elif paginas >= 2000 and paginas < 20000:
                desconto = paginas - (paginas * 0.25)
                return desconto
                break
            elif paginas >= 20000:
                print('Não aceitamos tantas paginas de uma vez.')
                print('Por favor, entre com o número de paginas novamente.')
                print('')

        except ValueError:
            print('Erro: Entrada inválida! Por favor, digite um número.')


def servico_extra():
    while True:
        try:
            print('Deseja adicionar algum serviço?')
            print(f'1 - Encadernação Simples - R$ {encs:.2f}')
            print(f'2 - Encadernação Capa Dura - R$ {encd:.2f}')
            print(f'0 - Não desejo mais nada')
            deseja = int(input('>>>'))

            if deseja == 1:
                return encs
            elif deseja == 2:
                return encd
            else:
                return 0
        except ValueError:
            print('Erro: Entrada inválida! Por favor, digite um número.')
            print('')


servico = escolha_servico()
paginas = num_pagina()
extra = servico_extra()

total = (servico * paginas) + extra

print(
    f'Total: R$ {total:.2f} (serviço: {servico:.2f} * páginas: {paginas:.0f} + extra: {extra:.2f})')
