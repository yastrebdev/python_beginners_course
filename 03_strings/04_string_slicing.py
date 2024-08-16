address = 'Altai, Barnaul'

area = address[:5] # or [0:5]
print(area)

city = address[7:] # or [7:14]
print(city)

oa = 'oaoaoaoaoaoaoao'
aa = oa[1::2] # or [1:len(oa) + 1:2]
print(aa)

reversed_address = address[::-1]
print(reversed_address)


website = "http://google.com"
my_slice = slice(7,-4)
print(website[my_slice])