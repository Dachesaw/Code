for age in range(1,100):
    if age < 2:
        print(f'{age} - Младенец')
    elif 4 > age >= 2:
        print(f'{age} - Малыш')
    elif 13 > age >= 4:
        print(f'{age} - Ребенок')
    elif 20 > age >= 13:
        print(f'{age} - Подросток')
    elif 65 > age >= 20:
        print(f'{age} - Взрослый')
    else:
        print(f'{age} - Пажилая артелерия')