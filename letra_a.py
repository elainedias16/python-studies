l = str(input('Type a frase:\n'))
line = l.lower()

num = line.count('a')  
print('The letter a appers {} times \n' .format(num))

ch = line.find('a')
print('The first time it appears is in caractere {}  \n' .format(num))

print('The last time it appears is in caractere {}  \n' .format(line.rfind('a')))
