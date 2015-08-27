def do_twice(f,value):
    f(value)
    f(value)
    
def print_twice(value):
    print value

do_twice(print_twice,'spam')