utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'fork'}

# utensils.remove('fork')
# utensils.add('napkin')
# utensils.clear()
# utensils.update(dishes)

dinner_table = utensils.union(dishes)

for u in dinner_table:
    print(u)

print(utensils.intersection(dishes))