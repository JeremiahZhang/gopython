# Search through lines
# Using 'find' method

def main():
    count = 0
    with open('mbox-short.txt') as f:
        for line in f:
            line = line.rstrip()
            if line.find('@uct.ac.za') == -1: continue
            count += 1
            print(line)
        
        print('Count: ', count)

if __name__ == '__main__':
    main()
