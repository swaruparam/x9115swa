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
        
grid(4,4)
    
      