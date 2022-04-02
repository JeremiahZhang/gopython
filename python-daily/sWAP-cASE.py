import string

def swap_case(s):
    res = ''
    for x in s:
        if x in string.ascii_lowercase:
            res += x.upper()
        else:
            res += x.lower()
    
    return(res)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''