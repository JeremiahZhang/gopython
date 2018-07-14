def fmax(lst):
    max_num = lst[0]
    for val in lst[1:]:
        if val > max_num:
            max_num = val
    return max_num

def fmin(lst):
    min_num = lst[0]
    for val in lst[1:]:
        if val < min_num:
            min_num = val
    return min_num

def main():
    numlist = []
    while True:
        inp = input('Enter a number: ')
        if inp == 'done': break
        try:
            value = float(inp)
            numlist.append(value)
        except:
            print('Enter a number please!')

    if len(numlist) > 0:
        val_max = fmax(numlist)
        val_min = fmin(numlist)
        print('Maximum: {}'.format(val_max))
        print('Minimum: {}'.format(val_min))

    print('Bye!')

if __name__ == '__main__':
    main()
