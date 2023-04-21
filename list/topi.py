available_toppings = ['соль', 'пиперони', 'сыр', 'перец', 'оливковое масло', 'песто']
requested_toppings = ['соль', 'бананы', 'песто']
if requested_toppings:
    for toping in requested_toppings:
        if toping in available_toppings:
            print(f'Добавленно - {toping}')
        else:
            print(f'Нету в наличии добавки - {toping}')
else:
    print('Если вы будете пиццу без добавок?\nНажмите продолжить')            