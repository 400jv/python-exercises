import random 
lista = []
name = str(input('Primeiro aluno: '))
lista.append(name)

name = str(input('Segundo aluno: '))
lista.append(name)

name = str(input('Terceiro aluno: '))
lista.append(name)

name = str(input('Quarto aluno: '))
lista.append(name)

print(f'O aluno escolhido foi {random.choice(lista)}')
