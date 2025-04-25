# meu codigo
soma = 0
resul = 0
media = 0

for i in range(1, 101, 1):
    if (i % 2 == 0):
        soma += i
        media += 1
resul = soma/media

print(soma)
print(media)
print(f'A média dos pares de 1 até 100 é: {resul}')