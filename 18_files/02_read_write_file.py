try:
    with open('file.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('That file was is not found! :(')

print(file.closed)


text = 'Yoooooooooo\nbro my broooo\n'

with open('file.txt', 'w') as file:
    file.write(text)

new_text = 'I am a new text'

with open('file.txt', 'a') as file:
    file.write(new_text)