import shutil
import os

# shutil.copyfile('file.txt', 'copy.txt')

source = 'copy.txt'
destination = 'D:\\Development\\python\\learn\\python_beginners_course\\copy.txt'

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source, 'was moved')
except FileNotFoundError:
    print(source, 'was not found!')


path = 'file.txt'
empty_folder = 'empty_folder'
folder = 'folder'

try:
    # os.remove(path)
    # os.rmdir(empty_folder)
    shutil.rmtree(folder)
except FileNotFoundError:
    print('That file was not found!')
except PermissionError:
    print('You do not have permission to delete that')
except OSError:
    print('You can not delete that using that function')
else:
    print(folder, 'was deleted!')