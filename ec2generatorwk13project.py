x= int(input('How many EC2 instances do you need names for? ' ))
department = input('What is the name of your department? ')
department = (input('Department: ')).lower()     
allowed = ['marketing', 'accounting', 'finops'] 
print('Here is your unique instance name:')
import random
import string
randomLetter = random.choice(string.ascii_letters)
for z in range(x):
    print(random.randrange(1,100), department,randomLetter)
else:
    print('Sorry, this generator is only for certain departments')
    # I used this line previously for line2 if department == 'Marketing' or 'marketing' or department == 'Accounting' or 'accounting' or department == 'FinOps' or 'finops':
