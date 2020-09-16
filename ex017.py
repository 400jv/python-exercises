import math

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa é: {pow((catetoOposto**2) + (catetoAdjacente**2), (1/2)):.2f}')
