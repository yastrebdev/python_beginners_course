animal = 'cow'
item = 'moon'

# print('The ' + animal + ' jumped over the ' + item)
print('The {} jumped over the {}'.format(animal, item))
print('The {1} jumped over the {0}'.format(animal, item))
print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))

text = 'The {} jumped over the {}'
print(text.format(animal, item))


name = 'Denis'
print('Hello, my name is {:10}. Nice to meet you'.format(name))
print('Hello, my name is {:>10}. Nice to meet you'.format(name))
print('Hello, my name is {:<10}. Nice to meet you'.format(name))
print('Hello, my name is {:^10}. Nice to meet you'.format(name))

pi = 3.14159
print('The number pi is {:.2f}'.format(pi))

number = 1000
print('The number is {:,}'.format(number))
print('The number is {:b}'.format(number))
print('The number is {:o}'.format(number))
print('The number is {:x}'.format(number))
print('The number is {:X}'.format(number))
print('The number is {:e}'.format(number))
print('The number is {:E}'.format(number))
