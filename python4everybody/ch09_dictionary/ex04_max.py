def max_find(dicts):
    max_value = None
    max_key = None
    for (key, val) in dicts.items():
        if max_value == None or max_value < val:
            max_value = val
            max_key = key
    return max_key

def main():
    fname = input('Enter a file name: ')
    if len(fname) < 1:
        fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    counts = dict()
    try:
        with open(fname) as fh:
            for line in fh:
                line = line.rstrip()
                if line.startswith('From '):
                    words = line.split()
                    counts[words[1]] = counts.get(words[1], 0) + 1
        
        max_key = max_find(counts)
        print(max_key, counts[max_key])
    except:
        print('File cannot be found', fname)
        exit()

if __name__ == '__main__':
    main()
