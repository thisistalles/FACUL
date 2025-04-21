preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o valor do desconto: R$'))


desc = preco*(desconto/100)
res = preco-desc
print(f'Seu desconto foi: R${desc}')
print(f'Valor final do produto: R${res}')
