#Author: Elaine Dias Pires

real= float(input('Please, type some amount of money R$'))
dolar = real / 3.27

print('Considering this amount of money and the cotation of dollar as R$3.27 , we could buy US${:.2f}'
.format(dolar))