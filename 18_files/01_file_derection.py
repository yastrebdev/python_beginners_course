import os

path = 'D:\\Development\\python\\learn\\python_beginners_course\\18_files\\file.txt'

if os.path.exists(path):
    print('That location exists!')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print('That is directory')
else:
    print('That location does not exists!')