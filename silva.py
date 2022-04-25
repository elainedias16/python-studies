name_aux = str(input('What\'s your name?\n'))

name = name_aux.lower()

if(name.find('silva') == -1):
    print('You doesn\'t have Silva in your name!\n')
else:
    print('The name Silva beggins in the caractere {} \n' .format(name.find('silva')))