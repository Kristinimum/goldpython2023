#if statements can be used inside another if statement
# multi level indentation is important to help designate nested if statements.
answer_a = input('Do you like traveling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')