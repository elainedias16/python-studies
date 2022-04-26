name_aux = str(input('What\'s your name?\n')).strip()

name = name_aux.lower()

print('Answer: {} ' .format('Silva' in name))

if(name.find('silva') == -1):
    print('You doesn\'t have Silva in your name!\n')
else:
    print('The name Silva beggins in the caractere {} \n' .format(name.find('silva')))