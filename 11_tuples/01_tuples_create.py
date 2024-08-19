student = ('Denis', 21, 'male')

print(student.count('Denis'))
print(student.index('male'))

for s in student:
    print(s)

if 'Denis' in student:
    print('Denis is here!')