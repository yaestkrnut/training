print(f"003 ***** f-strings")


name = "Cooper"
age = 239
print(f"My name is {name} - {age} years old")
print(f"Caps Name: {name.upper()}")


from math import pi
print(f"Value PI: {pi:.2f}")


from datetime import datetime as dt
now_time = dt.now()
print(f"Time {now_time:%d.%m.%Y %H:%M}")


y = 334
x = 56
z = 3
print(f"Mathematics {y} - {x} * {z} = {y - x * z}")


digits_list = [0,1,2,3,4,5,6,7,8,9]
print(f"Digit from list {digits_list[5]}")


words_dictionary = {'one':1, 'two':2}
print(f"Word from dict {words_dictionary['two']}")


print(f"Call func 13 / 3 = {round(13/3)}")


