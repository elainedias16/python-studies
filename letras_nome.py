#Author: Elaine Dias Pires

name = str(input('Type your name:\n'))

print('\n')
print(name.upper())
print(name.lower())

name_split = name.split()

print('\nThe first name has {} letters ' .format(len(name_split[0])))

qtd = 0
for i in range (0, len(name_split)) :
    qtd = qtd + len(name_split[i])

print('This entire name has {} letters ' .format(qtd))