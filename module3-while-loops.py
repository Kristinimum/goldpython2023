#while condition: while loops are also helpful when you don't know how many attempts a user might need like with a guessing game.
   # do_something ()
    #do_something2 ()
counter = 1
while counter < 11:
    print(counter)
    # the += shows to increase the counter value by 1 in this case. if you did not use that then you would have an infinite loop.
    counter += 1
print('Finished!')

secret_number = 14
print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')