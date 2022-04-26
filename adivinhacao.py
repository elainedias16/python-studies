#Author: Elaine Dias Pires

# import random
# num = random.randint(1,5)
# print(num)

from random import randint
num = randint(1,5)

print('Hello!Try to guess the number that computer has chosen! ')
num_user= int(input('Type a number between 1 to 5\n'))

if num_user==num :
    print('Congratulations, you got it!')
else:
    print('Not this time... try again!')