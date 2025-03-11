#5-8. Hello Admin

#user_list = ['ada', 'ceci', 'sebas', 'admin']

#for user in user_list:
    #if user == 'admin':
        #print(f'Hello {user.title()}, would you like to see status report?')
    #else:
        #print(f'Welcome! {user.title()} thank you for logging in again')

#5-9. No Users
#user_list = []
#if user_list:
    #for user in user_list:
        #print(f'Hello {user}')
#else:
    #print('We need to find some users')

##5-10. Checking usernames:
#current_users = ['ada','sebas','monica', 'edu', 'shirley']
#new_users = ['Monica', 'shirley']

#for user in new_users:
    #if user.lower() in current_users:
        #print(f'{user} you need a diferent user name')
    #else:
        #print('User name available')

##5-11. Ordinal Numbers
numbers =[1, 2, 3, 4, 5, 6, 7, 8,9]

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')