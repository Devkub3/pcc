#3-4. Guest list
guests = ['Ada', 'Sebas', 'Shiyi']
for i in guests:
    print(f'{i} You are invited to a poll party!!')

#3-5. Changing guest list
cant_comme = 'Shiyi'
guests.remove(cant_comme)
print(f'This guest cant come to the party {cant_comme}')

guests.append('Victor') 
for i in guests:
    print(f'{i} Your are invited to a poll party!!')

#3-6.More Guests
guests.insert(0,'Ruth')
guests.insert(2,'Marcos')
guests.append('Miguel')
for i in guests:
    print(f'{i} Your are invited to a poll party!!')

#3-7.Shrinking guest list
for invitados in guests:
    print(f'{invitados} por problemas tecnicos solo podran venir 2 personas')

guests.pop(0)
guests.pop(1)
guests.pop(-1)
guests.pop(2)
print(guests)
for invitados in guests:
    print(f'{invitados} invitados que vienen')

del guests[0]
guests.remove('Sebas')
print(guests)
