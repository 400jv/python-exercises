string = str(input('Digite algo: '))

print(f'O tipo primitivo é?   {type(string)}')
print(f'Só tem espaço?        {string.isspace()}')
print(f'É númerico?           {string.isnumeric()}')
print(f'É alfabético?         {string.isalpha()}')
print(f'É alfanúmerico?       {string.isalnum()}')
print(f'Está em maiúsculas?   {string.isupper()}')
print(f'Está em minúsculas?   {string.islower()}')
print(f'Está capitalizada?    {string.istitle()}')