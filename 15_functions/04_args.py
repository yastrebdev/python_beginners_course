def add(*args) -> int:
    sum = 0
    args = list(args)
    args[0] = 10
    for i in args:
        sum += i
    return sum

print(add(1, 2, 4))