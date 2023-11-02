inputs = list(map(int, input().split(', ')))


def logging_decorator(func):
    def wrapper(*args):
        result = f'You called {func.__name__}{args}\n'
        result2 = func(*args)
        result += f"It returned: {result2}"
        return result

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


res = a_function(inputs[0], inputs[1], inputs[2])
print(res)
