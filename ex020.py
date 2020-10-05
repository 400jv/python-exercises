from random import shuffle

alunos = list()

aluno = str(input("Primeiro Aluno: "))
alunos.append(aluno)

aluno = str(input("Segundo Aluno: "))
alunos.append(aluno)

aluno = str(input("Terceiro Aluno: "))
alunos.append(aluno)

aluno = str(input("Quarto Aluno: "))
alunos.append(aluno)

shuffle(alunos)
print(alunos)
