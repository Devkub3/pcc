#Creamos un lista vacia para almacenar aliens
aliens = []

#Creamos 30 aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'speed':'slow', 'points':5}
    aliens.append(new_alien)

#Cambiar color, velocidad y puntos
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:2]:   
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Mostramos los primeros 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

#Contamos el total de aliens creados en la lista
print(f'Total aliens en lista aliens {len(aliens)}')
