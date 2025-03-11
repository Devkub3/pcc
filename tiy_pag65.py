#4-10. Slices
comidas = ['pizza', 'hamburguesa', 'empanada', 'tortilla', 'tallarin', 'lomito',
          'mandioca', 'pan']
print(comidas[:3])
print(f'Three items from the middle of the list are{comidas[3:6]}')
print(f'The last three items are{comidas[-3:]}')

#4-11.My Pizzas, Your pizzas 
my_pizzas = ['peperoni', 'jam and cheese', 'napo', 'pinaple']
your_pizzas = my_pizzas[:]
my_pizzas.append('meat')
your_pizzas.append('vegetarian')

for pizza in my_pizzas:
    print(f'My favorite pizzas are {pizza.title()}')

for pizza in your_pizzas:
    print(f'My friends favorite pizzas are {pizza.title()}')

#4-12.More Loops
my_foods = ['pizza','falafel', 'carrot cake']
for food in my_foods:
    print(food.title())

