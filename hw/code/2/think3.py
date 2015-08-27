#print "Output of Excercise 3.1"

#repeat_lyrics()

#def print_lyrics():
#    print "I'm a lumberjack, and I'm okay."
#    print "I sleep all night and I work all day."

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
    
print "\nOutput of Excercise 3.2"    

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

print "\nOutput of Excercise 3.3"

def right_justify(s):
    s_len = len(s)
    result = " " * (70-s_len)
    result += s
    return result
    
print right_justify("Swarupa")

print "\nOutput of Excercise 3.4"

def do_twice(f,value):
    f(value)
    f(value)
    
def print_twice(value):
    print value
    
def do_four(f,value):
    do_twice(f,value)
    do_twice(f,value)

do_four(print_twice,'spam')

print "\nOutput of Excercise 3.5.1"

def grid (row,col):
    row = 5*(row-1) +1
    col = 5*(col-1) +1
    for i in range(0,row):
        for j in range(0,col):
            if i%5 == 0 and j%5 == 0:
                print "+",
            elif i%5 == 0:
                print "-",
            elif j%5 == 0:
                print "/",
            else:
                print " ",
        print
        
grid(3,3)

print "\nOutput of Excercise 3.5.2"

grid(4,4)
