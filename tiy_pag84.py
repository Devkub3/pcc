#5-3.Alien Colors #1

#pick = input('Please choose a color between green, yellow or red: ')
#alien_color = ['green', 'yellow', 'red']

#if pick == 'green':
#    print('You earned 5 points')
#elif pick =='yellow':
#    print('You earned 10 points')
#else:
#    print('You earned 15 points')


#5-6. Stages of Life
#age = int(input('Please add your age: '))
#if age < 2:
#    print('Is a baby')
#if age >= 2 and age < 4:
#    print('Is a toddler')
#if age >=4 and age < 13:
#    print('Is a kid')
#if age >= 13 and age < 20:
#    print('Is a Teenager')
#if age >= 20 and age < 65:
#    print('Is an adult')
#else:
#    print('Is an elder')

#5-7. Stages of life
favorite_fruits = ['apple', 'orange', 'banana']

for fruit in favorite_fruits:
    fruit = input('write a fruit of your preference: ')
    if fruit in favorite_fruits:
        print(f'You really like {fruit}!')
    else:
        print('ERROR 404 fruit not found')