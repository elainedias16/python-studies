#Author: Elaine Dias Pires

name = str(input('Type your name:\n')).strip()

print('\n')
print(name.upper())
print(name.lower())

name_split = name.split()
n = len(name_split)

print('\nYour first name is {} ' .format(name_split[0]))
print('\nYour last name is {} ' .format(name_split[n-1]))

