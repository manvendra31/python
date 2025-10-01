# Swipe the string from capital letter to small letter

def swap_case(s):
    new_s = ''
    for i in s:
        if i.upper() == i:
            new_s += i.lower()
        else:
            new_s += i.upper()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)