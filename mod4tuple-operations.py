user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')
    
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)
    
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print('This person comes from the US!') # the + creates a new tuple with all the new and old data

numbers = (0, 1) * 10
print(numbers)
