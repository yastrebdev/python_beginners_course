BASE_HEALTH = 100

character_name = input('Named your character: ')
print('Your character name:', character_name)

start_level = input('Start level: ')
start_level = int(start_level)

health = BASE_HEALTH * start_level
print(character_name + ':', '(level - ' + str(start_level) + ')', 'health - ' + str(health))

# special cases

# coins = int(input('How many coins: ')) # ValueError: invalid literal for int() with base 10: '12.2'
coins = float(input('How many coins: '))
coins += 1

print('Your coins: ' + str(coins))