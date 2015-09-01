def has_duplicates(check_list):
    temp_list = [ ]
    for item in check_list:
        if item not in temp_list:
            temp_list.append(item)
        else:
            return True
    return False
    
print has_duplicates(['a','a','c'])
    