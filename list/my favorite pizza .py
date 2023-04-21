pizza = ['пеперони', 'маргарита', '4-ре сыра', 'деревенская', 'мексиканская']
my_favorite_pizza = pizza
friend_favorite_pizza = my_favorite_pizza
pizza.append('гавайская')
friend_favorite_pizza.append('индийская')
my_favorite_pizza.append('с колбасой')

for food in pizza:
    print(f'Пицца - {food.title()}')








#print(f'Мне нравиться пицца: {my_favorite_pizza}\nМоим друзьям нравиться пицца: {friend_favorite_pizza}')