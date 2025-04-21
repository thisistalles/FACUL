km = int(input('Quantos Km foram pecorrido?: '))
dias = int(input('Por quantos dias o carro foi alugado?: '))

calculo = (dias*60) + (km*0.15)
print(f'Dias: {dias}, KM: {km}.')
print(f'Valor final: {calculo}')

