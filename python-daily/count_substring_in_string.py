def count_substring(string, sub_string):
    """ Count sub_string in string.
    Such as:
    Input:
        ABCDCDC
        CDC
    Output:
        2
    """
    len_str = len(string)
    len_sub = len(sub_string)
    count = 0
    for i in range(0, len_str - len_sub + 1):
        if string[i:(i+len_sub)] == sub_string:
            count += 1
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)