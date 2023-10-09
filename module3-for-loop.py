#for loops are used in Python to go through all the particular elements in a sequence
# in introduces the range of possible values or sequences that we should scan. scan iscalled iterating
for letter in 'hello!':
    print('Current letter:', letter)
    #range is a function value. remember stop value is not included
for counter in range(1,11):
    print(counter)
    # the += shows to increase the counter value by 1 in this case. if you did not use that then you would have an infinite loop.
print('Finished!')    