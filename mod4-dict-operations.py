grades = {}
#add entries with square brackets like this:
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
#to update an value like a grade improvement do:
grades['Anne'] = 'A'
print(grades)
#update method using .update after the name of our dictionary
grades.update({'John':'A'})
print(grades)
#this update method is not as quick as previous method above.
len(grades)
print(len(grades)) #with this example it will be 2

if 'John' in grades:
    print('John got:', grades['John'])

del grades['John']
print(grades)
#iterating a dictionary with either a for loop. there is the keys method. the third method gets access to keys and values
for el in grades:
    print (el)
for el in grades.keys():
    print(el)
#can use values to get access to values
for el in grades.values():
    print(el)
#3rd method gets access to keys and values
for person, grade in grades.items(): #we used 2 control variables separated by a comma, person and grade.
    print(person, 'got', grade)

