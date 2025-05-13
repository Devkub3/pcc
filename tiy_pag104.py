#6-4. Glossary 2
#---
#dicc = {'if':'sentencia si evalua', 'else':'condicion final', 'elif':'condicion opcion'}
#for k, v in dicc.items():
#    print(f'key is {k} and value is {v}')

#---
#6-5 Rivers
#rivers = {'egipto':'nilo', 'paraguay':'paraguay', 'brasil':'amazonasp'}
#for v in rivers.values():
#    print(f'{v}')

#---
#6-6. Polling
fav_lang = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python','edu':'','ada':''}
take_poll = ['edu', 'ada']

for n in fav_lang.keys():
    print(f'Hi {n.title()}.')
    if n in take_poll:
        lang = fav_lang[n].title()
        print(f'{n.title()} please take the poll ')