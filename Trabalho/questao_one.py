print('Bem-vindo a Loja do Talles Robert')
valor_unitario = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))


calculo = valor_unitario * quantidade
desconto = 0
porcentagem = 0

if calculo >= 2500 and calculo < 6000:
    porcentagem = 0.04 * calculo
    desconto = calculo - porcentagem

elif calculo >= 6000 and calculo < 10000:
    porcentagem = 0.07 * calculo
    desconto = calculo - porcentagem

elif calculo >= 10000:
    porcentagem = 0.11 * calculo
    desconto = calculo - porcentagem
else:
    calculo < 2500
    
print(f'O valor SEM desconto: R${calculo}')
print(f'O valor COM desconto: R${desconto}')
