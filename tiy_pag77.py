#5-1. Conditional tests
car = 'subaru'
#print('Is car == subaru?, I predict = True')
#print(car == 'subaru')

pc = 'hp'
#print('Is pc == hp?, I predict = False')
#print(pc == 'Asus')

#5-2. more conditional tests
string1 = 'HOLA'
string2 = 'hola'
#print(string1.lower() == string2)

num1 = 10
num2 = 20
num3 = 20
num4 = 20
#print(num1 >= num2)
#print(num1 == num2 and num3 == num4)
#print(num1 > num2 or num3 > num4)


nombre = input('Ingresa nombre de alguna persona que conozcas: ')
conocido = ['marta', 'adri', 'kari']

if nombre.lower() in conocido:
    print(f'Conoces a {nombre.title()}')
else:
    print(f'No conoces a {nombre.title()}')
