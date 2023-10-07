user_age = int(input('How old are you?'))
person = input('Are you a dog or cat person?')

if user_age < 25 and person == 'Dog person':
    print('You qualify for a puppy!')
else:
    print('Sorry you are owned by a cat!')


user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange programme')
else:
    print('Sorry, you do not qualify')
    
    
user_country = input('What is your country?')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')    
    
    #order of joining multiple conditions that python considers
    # 1. not 2. and 3. or
    