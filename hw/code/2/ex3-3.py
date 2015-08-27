def right_justify(s):
    s_len = len(s)
    result = " " * (70-s_len)
    result += s
    return result
    
print right_justify("Swarupa")