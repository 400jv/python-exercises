from time import sleep

nome = input('Digite seu nome completo: ')

print('Analisando seu nome...')
sleep(.5)

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")

primeiroNome = nome.split(' ')[0]
print(f"Seu primeiro nome é {primeiroNome} e ele tem {len(primeiroNome)} letras")
