fav_band = 'Green Day'
print(fav_band[6])
print(fav_band[:6])

#strings have many methods and can look them up in Python documentation
text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)

user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')