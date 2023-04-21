users = ['Admin', 'Jake', 'smolusha04', 'Nexo']
if users:
    for user in users:
        if user.lower() != 'admin':
            print(f'Добро пожаловать на сайт - {user}')
        else:
            print('Приветствую верховный администратор')
else:
    print('Список пользователей пуст')