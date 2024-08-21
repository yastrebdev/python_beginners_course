class Dragon:

    wings = 2 # class variable

    def __init__(self, *, color):
        self.color = color # instance variable

print(Dragon.wings)

Dragon.wings = 4
print(Dragon.wings)

red_dragon = Dragon(color='red')
green_dragon = Dragon(color='green')

green_dragon.wings = 2

print(red_dragon.wings)
print(green_dragon.wings)