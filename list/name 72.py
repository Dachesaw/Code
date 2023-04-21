favorite_number = {'daniil': 72,
                   'smolusha': 69,
                   'boria': 27,
                   'kazia': 90,
                   'matvei': 84}
friend = ['matvei', 'boria']
for name in favorite_number.keys():
    print(name.title())

    if name in friend:
        number = favorite_number[name]
        print(f'\t{name.title()}, твоя любимая цифра {number}')