name = None

while not name:
    name = input('Enter your name: ')

print('Hello', name)


health = 100

while health > 0:
    health -= 20
    print(name, 'took damage: -20hp')
    print(name, 'hp =', health)

if health <= 0:
    print(name, 'is dead')