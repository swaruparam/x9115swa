def do_twice(f,value):
    f(value)
    f(value)
    
def print_twice(value):
    print value
    
def do_four(f,value):
    do_twice(f,value)
    do_twice(f,value)

do_four(print_twice,'spam')

