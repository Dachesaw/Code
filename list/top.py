
requested_toppings = ['сахар', 'соль', 'кетчуп', '+ 2']
if requested_toppings:
    for requsted_top in requested_toppings:
        if requsted_top == 'кетчуп':
            print('Кетчупа в наличии')
        else:
            print(f'Вы добавили - {requsted_top}')
else:
    print('Доступна базовая пицца')