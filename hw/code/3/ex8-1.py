def has_duplicates(check_list):
    temp_list = [ ]
    for item in check_list:
        if item not in temp_list:
            temp_list.append(item)
        else:
            return True
    return False

inp = ['a','a','c'] 
print inp
print has_duplicates(inp)
inp = ['a','b','c']
print inp
print has_duplicates(inp)