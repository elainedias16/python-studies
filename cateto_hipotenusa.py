#Author: Elaine Dias Pires

import math 

op = float(input('Digite o cateto oposto de um triangulo retangulo:\n'))
adj = float(input('e o cateto adjacente: \n'))

h = math.sqrt( pow(op,2) + pow(adj,2) )

print('A hipotenusa desse triangulo eh {:.2f} ' .format(h))