age = int(input('Введите возраст: '))
if age < 4:
    price = 0
    old = "ребенок"
elif age < 18:
    price = 400
    old = 'подросток'
elif age >= 65:
    price = 150
    old = 'пенсионер'
elif age <= 65:
    price = 800
    old = 'взрослый'

print(f'Тариф: {old.title()}\nВаш билет будет стоить {price} рублей')