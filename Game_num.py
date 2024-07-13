from random import randint
name_p1 = input('Введите имя первого игрока: ')
name_p2 = input('Введите имя второго игрока: ')
num_p1 = int(input('Первый игрок вводит число от 1 до 6: '))
num_p2 = int(input('Второй игрок вводит число от 1 до 6: '))
num = randint(1, 6)
if num_p1 == num:
    print('Победил', name_p1)
elif num_p2 == num:
    print('Победил', name_p2)
else:
    print('Попробуйте ещё раз')

