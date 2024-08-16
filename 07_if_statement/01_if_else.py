credit_rating = input('Please, say your rating?: ')

if credit_rating.isdigit():
    credit_rating = int(credit_rating)
else:
    print('Enter a number')

if credit_rating >= 120:
    print('The loan is approved')
elif 60 <= credit_rating < 120: # not credit_rating > 120 and credit_rating <= 60
    print('We can offer you a credit card')
else:
    print('The loan is not approved')


slot = input('What was the number?: ')

if slot == 777:
    print('Jackpot')
elif slot != 777:
    print('not Jackpot')