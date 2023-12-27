import math

def oplata(km):
    m = km * 1000
    metraj = m / 140
    groshi = 240 + (metraj * 15)
    return(round(groshi))

print(f'У меня тут по счётчику столько выходит {oplata(float(input()))} рублей')