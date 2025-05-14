
cp_p = 9.00
cp_m = 14.00
cp_g = 18.00

ac_p = 11.00
ac_m = 16.00
ac_g = 20.00

print('Bem-Vindo a Loja de Gelados do Talles Robert')
print(20 * '-', 'Cardápio', 23 * '-')
print(53 * '-')

print(f'---| Tamanho   |   Cupuaçu (CP)  |    Açai (AC)  |---       ')
print(f'---|    P      |   R$ {cp_p:.2f}       |    R$ {ac_p:.2f}   |---')
print(f'---|    M      |   R$ {cp_m:.2f}      |    R$ {ac_m:.2f}   |---')
print(f'---|    G      |   R$ {cp_g:.2f}      |    R$ {ac_g:.2f}   |---')

print(53 * '-')

valor = 0
while True:

    sabor = input('Entre com o sabor desejado (CP/AC): ')
    saborM = sabor.upper()

    if not saborM == 'AC' and not saborM == 'CP':
        print('Sabor inválido. Tente novamente')
        print('')
        continue

    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    tamanhoM = tamanho.upper()

    if not tamanhoM == 'P' and not tamanhoM == 'M' and not tamanhoM == 'G':
        print('Tamanho inválido. Tente novamente')
        print('')
        continue

    if saborM == 'CP' and tamanhoM == 'P':
        print(f'Você pediu um Cupuaçu no tamanho {tamanhoM}: R${cp_p:.2f}')
        valor += cp_p
    elif saborM == 'CP' and tamanhoM == 'M':
        print(f'Você pediu um Cupuaçu no tamanho {tamanhoM}: R${cp_m:.2f}')
        valor += cp_m
    elif saborM == 'CP' and tamanhoM == 'G':
        print(f'Você pediu um Cupuaçu no tamanho {tamanhoM}: R${cp_g:.2f}')
        valor += cp_g

    elif saborM == 'AC' and tamanhoM == 'P':
        print(f'Você pediu um Açai no tamanho {tamanhoM}: R${ac_p:.2f}')
        valor += ac_p
    elif saborM == 'AC' and tamanhoM == 'M':
        print(f'Você pediu um Açai no tamanho {tamanhoM}: R${ac_m:.2f}')
        valor += ac_m
    elif saborM == 'AC' and tamanhoM == 'G':
        print(f'Você pediu um Açai no tamanho {tamanhoM}: R${ac_g:.2f}')
        valor += ac_g

    coisa = input('Deseja mais alguma coisa? (S/N): ')
    coisam = coisa.upper()
    print('')

    if coisam != 'S':
        print('')
        print(f'O valor total a ser pago: R${valor:.2f}')
        break
