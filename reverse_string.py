def reverse_string(s:str):
    reverse_str = ""
    index = len(s)
    while index != 0:
        reverse_str += s[index-1]
        index -= 1
    return reverse_str
    #my code here


print(reverse_string('hello'))