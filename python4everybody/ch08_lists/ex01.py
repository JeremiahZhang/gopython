def chop(t):
    t_one = t[1:]
    t_one.pop()
    return None

def middle(t):
    t_two = t[1:]
    t_two.pop() 
    return(t_two)

def main():
    t = [1, 2, 3, 4, 5]
    t_one = chop(t)
    t_two = middle(t)
    print(t_one)
    print(t_two)

if __name__ == '__main__':
    main()
