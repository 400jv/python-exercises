from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo que você deseja: '))
radian = radians(ang)

print(f'O ângulo de {ang} tem o seno de {sin(radian):.2f}')
print(f'O ângulo de {ang} tem a tagente de {tan(radian):.2f}')
print(f'O ângulo de {ang} tem o cosseno de {cos(radian):.2f}')
