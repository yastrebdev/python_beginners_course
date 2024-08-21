def hello(**kwargs):
    # print('Hello', kwargs['last_name'], kwargs['first_name'], kwargs['middle_name'])
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(f'{value}', end=' ')

hello(title='Mr.', last_name='Yastrebov', first_name='Denis' , middle_name='Dmitrievich')