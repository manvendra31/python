# We can import any module and their some variable
# here we can import all the module
import random
#by second method


# from random import choice


# now we ca choose random number from 1-10
num=random.randint(1,10)
print(num)


# Now we can suffel or rearrange
num1=["Jack","King","Queen","Manvendra"]
random.shuffle(num1)
for card in num1:
    print(card)