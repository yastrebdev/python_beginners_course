usernames = ['Dude', 'Bro', 'Mister']
passwords = ('p@ssword', 'abc123', 'guest')
login_date = ['1/1/2001', '2/1/2001', '3/1/2001']

users = dict(zip(usernames, passwords))

print(users)

for key, value in users.items():
    print(key, value)

new_users = zip(usernames, passwords, login_date)

for i in new_users:
    print(i)