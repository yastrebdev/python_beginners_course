name = 'denis Developer'

if name[0].islower():
    name = name.capitalize()

first_name = name[0:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_character)