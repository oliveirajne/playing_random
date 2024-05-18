import random

int_min = 4
int_max = 8

dec_min = 0
dec_max = 9

def randomInt():
    return random.randint(int_min,int_max)
    
def randomDec():
    return random.randint(dec_min,dec_max)

num_int = randomInt()
num_dec = randomDec()

print(f'Nota aleatória (de {int_min},{dec_min} a {int_max},{dec_max})::::::::::: {num_int},{num_dec}')
