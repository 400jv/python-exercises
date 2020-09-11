preco = float(input('Qual é o preço do produto: R$'))

print(f'O produto custava R${preco} com um desconto de 5% vai custar R${preco - ((preco*5)/100):.2f}')
