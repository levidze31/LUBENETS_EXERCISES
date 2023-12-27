A, B, C = int(input('Введите сторону прямоугольника =')), int(input('Введите  другую сторону прямоугольник =')), int(input('Введите сторону квадрата ='))
CvA, CvB = 0, 0
znach = 0

while A >= C:
    A -= C
    CvA += 1

while B >= C:
    B -= C
    CvB += 1

for i in range(CvB):
    znach += CvA
print(f'Количество квадратов - {znach}')