_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())