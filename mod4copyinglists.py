name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)
#this does not work the same for lists. to copy lists you would need to
list_original = [1, 2, 3]
list_new = list_original[:] #this is called slicing
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new) 
#summarizing what this module entailed
list_original = [1, 2, 3]
list_new = list_original[:]#this will use slicing and not alter the original list

list_original = [1, 2, 3]
list_new = list_original #this will make these 2 lists have the same source so if you change one it will change the other.