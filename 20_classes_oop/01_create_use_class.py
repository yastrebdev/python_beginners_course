from _auxiliary_files.car import Car

car_1 = Car(make='Chevy', model='Corvette', year='2021', color='blue')
car_2 = Car(make='Ford', model='Mustang', year='2022', color='red')

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()