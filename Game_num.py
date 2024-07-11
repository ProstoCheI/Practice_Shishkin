from random import randint
num_p1 = int(input('Введите число первого игрока:'))
num_p2 = int(input('Введите число второго игрока: '))
num = randint(1, 6)
if num_p1 == num:
    print('Победил первый игрок')
elif num_p2 == num:
    print('Победил второй игрок')
else:
    print('Ничья')
