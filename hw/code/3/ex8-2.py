import random as r
count = 0
students = 23
no_simulations = 1000
    
def gen_bdays(students):
    random_bdays = [ ]
    for student in range(students):
        random_bday = r.randint(1,365)
        random_bdays.append(random_bday)
    return random_bdays

def has_duplicates(check_list):
    temp_list = [ ]
    for item in check_list:
        if item not in temp_list:
            temp_list.append(item)
        else:
            return True
    return False

def birthday():
    global count
    random_bdays = gen_bdays(students)
    checking = has_duplicates(random_bdays)
    if checking == True:
        count = count + 1
    return count

def simulations():
    # For multiple simulations of similar scenario
    for i in range(no_simulations):
        c = birthday()
    prob = float(c)/no_simulations
    return prob
    
print "No of students = ", students
print "No of simulations = ", no_simulations
print "Probability of two persons having the same birthday = ", simulations()
