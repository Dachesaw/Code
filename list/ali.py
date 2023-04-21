aliens = []
for aliens_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yelow'
        alien['points'] = 10
for al in aliens:
    print(al)