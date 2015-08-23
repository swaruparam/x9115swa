import time
from ok import *
  
print time.strftime("%H:%M:%S\n")

@ok
def _ok1():
    assert 1==1
 
@ok
def _ok2():
    assert 2==1

@ok
def _ok3():
    assert 3==3 

@ok
def _ok4():
    assert 4==3

@ok
def _ok5():
    assert 5==5
    
@ok
def _ok4():
    assert unittest.tries==6
    assert unittest.fails==2
    print unittest.score()
