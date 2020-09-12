days = int(input('Quantos dias alugados: '))
km = float(input('Quantos km rodados: '))

print(f'O total a pagar é R${(days * 60) + (km * 0.15):.2f}')
