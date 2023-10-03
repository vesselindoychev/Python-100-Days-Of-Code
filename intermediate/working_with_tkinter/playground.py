def add(*args):
    return sum(args)


print(add(1, 2, 3))


def calculate(**kwargs):
    print(kwargs)


calculate(a=1, b=2)
