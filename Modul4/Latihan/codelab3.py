_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"


def title_decoration(function):
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " " + "-Data is convert to title case")
        return make_title
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        split_string = func.split()
        print(str(split_string) + " " + "- Then Data is splitted")
        return split_string
    return wrapper

@split_string
@title_decoration
def say_hi():
    return "helo there"

say_hi()
