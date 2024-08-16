height = 5      # int
width = 8.2     # float
square = '41'   # str

print('01 -', height, width, square)


height = float(height)
print('02 -', height)

height = str(height)
print('02 -', height)
print('02 -', type(height))


width = int(width)
print('03 -', width)

width = str(width)
print('03 -', width)
print('03 -', type(width))


square = int(square)
print('04 -', square)

square = float(square)
print('04 -', square)

# features of behavior

x = 5
y = '5'
# print(x + y) - TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(x - y) - TypeError: unsupported operand type(s) for -: 'int' and 'str'
# print(x / y) - TypeError: unsupported operand type(s) for /: 'int' and 'str'
print('05 -', x * y) # 55555

a = 3
b = 3.0
print('06 -', a + b) # 6.0
print('06 -', a - b) # 0.0
print('06 -', a * b) # 9.0
print('06 -', a / b) # 1.0
