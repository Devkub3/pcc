#3-8.Seeing the world

place = ['machupichu', 'eurotrip','piramids','greatwall','kilimanjaro']
print(f'{place} 1')

print(f'{sorted(place)} 2')
print(f'{sorted(place, reverse=True)} 3')

place.reverse()
print(f'{place} 4')

place.reverse()
print(f'{place} 5')

place.sort()
print(f'{place} 6')

place.sort(reverse=True)
print(f'{place} 7')

#3-9. Dinner Guests
guests = ['Ada', 'Sebas', 'Shiyi']
print(len(guests))

#3-10.Every Function
paises = ['paraguay','argentina','brasil','uruguay','chile','colombia']
paises.sort()
print(f'{paises} 1')

paises.sort(reverse=True)
print(f'{paises} 2')

print(f'{sorted(paises)} 3')

print(f'{sorted(paises, reverse=True)} 4')

print(f'{len(paises)}')

print(paises[-1])