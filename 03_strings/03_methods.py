skill = 'armageddon'

print('01 -', len(skill)) # 10

print('02 -', skill.find('n')) # 9

print('03 -', skill.capitalize()) # Armageddon

print('04 -', skill.upper()) # ARMAGEDDON

skill_upper = skill.upper()

print('05 -', skill_upper.lower()) # armageddon

print('06 -', skill.isdigit()) # False

print('07 -', skill.isalpha()) # True

print('08 -', skill.count('a')) # 2

print('09 -', skill.replace('d', 'b')) # armagebbon

# not method
print('10 -', skill * 3)