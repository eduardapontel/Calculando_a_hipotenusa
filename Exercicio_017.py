from math import hypot

bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CALCULANDO A HIPOTENUSA'))
print(bordas)
print()

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
# print('A hipotenusa é igual a {:.2f}'.format((co**2+ca**2)**(1/2)))
print('A hipotenusa tem o comprimento igual a {:.2f}'.format(hypot(co, ca)))