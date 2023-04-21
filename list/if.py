banned_users = ['marie', 'andrew', 'kriper2004', 'ugl2']
user = 'jake2003'
if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish')
else:
    print(f'{user.title}, have been blocked')