cp_p = 9.00
cp_m = 14.00
cp_g = 18.00

ac_p = 9.00
ac_m = 14.00
ac_g = 18.00

print('Bem-Vindo a Loja de Gelados do Talles Robert')
print(20 * '-', 'Cardápio', 23 * '-')
print(53 * '-')

print(f'---| Tamanho   |   Cupuaçu (CP)  |    Açai (AC)  |---       ')
print(f'---|    P      |   R$ {cp_p:.2f}       |    R$ {ac_p:.2f}    |---')
print(f'---|    M      |   R$ {cp_m:.2f}      |    R$ {ac_m:.2f}   |---')
print(f'---|    G      |   R$ {cp_g:.2f}      |    R$ {ac_g:.2f}   |---')

print(53 * '-')

tamanho = ''
yn = 's'

sabor = input('Entre com o sabor desejado (CP/AC): ')

while yn == 's':

    if sabor != 'ac' and sabor != 'cp':
        print('Sabor inválido. Tente novamente')
        sabor = input('Entre com o sabor desejado (CP/AC): ')
    else:
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')

    if tamanho != 'p' or tamanho != 'm' or tamanho != 'g':
        print('Tamanho inválido. Tente novamente')
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    else:
        print('Você pediu um ')
