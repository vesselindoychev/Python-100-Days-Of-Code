import time


def make_bold(func):
    def wrapper():
        res = func()
        return f'<b>{res}</b>'

    return wrapper


def make_italic(func):
    def wrapper():
        res = func()
        return f'<i>{res}</i>'

    return wrapper


def make_underlined(func):
    def wrapper():
        res = func()
        return f'<u>{res}</u>'

    return wrapper


def delay_function(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()

        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper


@delay_function
@speed_calc_decorator
def say_hello():
    time.sleep(2)
    print('Hello')


@speed_calc_decorator
def say_bye():
    print('Bye')


def say_greeting():
    print('How are you?')


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i *= i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i *= i


fast_function()
slow_function()
