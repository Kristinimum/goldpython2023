#lists can have other lists with in them.
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
print(cells[0][0]) #this prints the first index 0
print(cells[1][2]) #this prints the 2nd index from the 2nd list
#to access individual elements need to use nested for loops
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
        #nested loops are used to help with tables
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)
        
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='') #this will make it look like a table
    print()

#create a list to represent the following table
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

