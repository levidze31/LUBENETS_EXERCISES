def krisa():
    C = (katet1 ** 2 + katet2 ** 2) ** 0.5
    return(C)

katet1 = float(input('Первый катет равен '))
katet2 = float(input('Второй катет равен '))

print(f'Гипотенуза равна {krisa()}')