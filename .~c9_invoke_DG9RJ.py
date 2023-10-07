x= int(input('How many EC2 instances do you need names for? ' ))
department = input('What is the name of your department? ')
if department == 'Marketing' or 'marketing' or department == 'Accounting' or 'accounting' or department == 'FinOps' or 'finops':
    print('Here is your unique instance name:')
    import random
    import string
    randomLetter = random.choice(string.ascii_letters)
    for z in range(x):
    import random
else:
    print('Sorry, this generator is only for certain departments')