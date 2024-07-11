from random import randint
name_p1 = input('Введите имя первого игрока: ')
name_p2 = input('Введите имя второго игрока: ')
num_p1 = int(input('Первый игрок вводит число: '))
num_p2 = int(input('Второй игрок вводит число: '))
num = randint(1, 6)
if num_p1 == num:
    print('Победил', name_p1)
elif num_p2 == num:
    print('Победил', name_p2)
else:
    print('Попробуйте ещё раз')

