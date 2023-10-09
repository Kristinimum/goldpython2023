#if we want to create a list from 1-100 we could use a loop.
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)


numbers = [i for i in range(1, 101)]  #it is important that the i variable comes before the loop, otherwise you will get an error
print(numbers)

numbers = [i for i in range(1, 101) if i % 3 != 0] #this skips numbers divided by 3
print(numbers)
