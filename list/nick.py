current_users = ['smolusha04', 'jake', 'nexo', 'grizzly']

new_users = ['SMOLUSHA04', 'host', 'Nexo']
if new_users:
    for users in new_users:
        if users.lower() in current_users:
            print(f'Такой никнейм уже существует - {users}')
        else:
            print(f'Вы успешно зарегестрировались - {users}')
else:
    print('Новых пользователей нету')