from math import hypot

bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CALCULANDO A HIPOTENUSA'))
print(bordas)
print()

co = ''
ca = ''

while type(ca) != float:
    try:
        ca = float(input('Digite o comprimento do cateto oposto: '))
    except:
        print('Por favor digite um comprimento válido!')

while type(co) != float:
    try:
        co = float(input('Digite o comprimento do cateto adjacente: '))
    except:
        print('Por favor digite um comprimento válido: ')

# print('A hipotenusa é igual a {:.2f}'.format((co**2+ca**2)**(1/2)))
print('A hipotenusa tem o comprimento igual a {:.2f}'.format(hypot(co, ca)))
