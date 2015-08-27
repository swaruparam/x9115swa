def do_twice(f,value):
    f(value)
    f(value)
    
def print_spam(value):
    print value

do_twice(print_spam,'spam')