first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first = second
second = first
print('After swapping:', first, second)

#modify this code a bit so that it will actually swap positions
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)

# there is a short cut also:first, second = second, first
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities) #this swaps spots of 0 and 4 index spots

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities) #this will sort in alphabetical order

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers) #this is how you sort for numbers

#reverse order. sort changes the list. but if you use sorted then it won't change original list.
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)