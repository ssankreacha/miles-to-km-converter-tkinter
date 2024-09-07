def add(*args):
    list = [int(each_number) for each_number in args]
    total = sum(list)
    return total

print(add(1, 1, 5, 6, 7, 8))

# for each number in the args, add each number in the array


def calculate(**kwargs):
    print(kwargs)

calculate(n1=1, n2=4, n3=6, n4=7)

