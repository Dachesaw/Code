favorite_number = {'daniil': 72,
                   'smolusha': 69,
                   'boria': 27,
                   'kazia': 90,
                   'matvei': 89
                   }
survey_participants = ['daniil', 'smolusha', 'boria', 'kazia', 'matvei', 'veronika', 'john']
for name in favorite_number:
    if 'daniil' == name:
        print(f'{name.title()} спасибо что поучавстовал в опросе')
    elif 'smolusha' == name:
        print(f'{name.title()} спасибо что поучавстовал в опросе')
    elif 'boria' == name:
        print(f'{name.title()} спасибо что поучавстовал в опросе')
    elif 'kazia' == name:
        print(f'{name.title()} спасибо что поучавстовал в опросе')
    elif 'matvei' == name:
        print(f'{name.title()} спасибо что поучавстовал в опросе')
    elif 'veronika' == name:
        print(f'{name.title()} спасибо что поучавстовал в опросе')
    else:
        print('Поучавствуй в опросе')
        
        # Я не понял как вывести тех кто не учавствал в опросе