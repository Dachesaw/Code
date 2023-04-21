people = []

d = {'first': 'daniil',
     'last': 'chesakov',
     'age': 18,
     'city': 'spb'}
for k, v in d.items():
    host = (f'{k}: {v}')
    people.append(host)
print(people)
for pip in people:
    print(pip)