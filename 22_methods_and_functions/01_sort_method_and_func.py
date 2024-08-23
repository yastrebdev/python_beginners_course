# students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr. Crabs']
# students = ('Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr. Crabs')

# students.sort(reverse=True)
# sorted_students = sorted(students, reverse=True)

# for i in students:
#     print(i)


# students = [
#     ('Squidward', 'F', 60),
#     ('Sandy', 'A', 33),
#     ('Patrick', 'D', 36),
#     ('Spongebob', 'B', 20),
#     ('Mr. Crabs', 'C', 78)
# ]

students = (
    ('Squidward', 'F', 60),
    ('Sandy', 'A', 33),
    ('Patrick', 'D', 36),
    ('Spongebob', 'B', 20),
    ('Mr. Crabs', 'C', 78)
)

# grade = lambda grades:grades[1]
# students.sort(key=grade, reverse=True)

age = lambda ages:ages[2]
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)