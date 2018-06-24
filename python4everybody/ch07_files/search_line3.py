# Search through line 
# Using 'continue'

def main():
    with open('mbox-short.txt') as fhand:
        for line in fhand:
            line = line.rstrip()
            # Skip 'uninteresting lines'
            if not line.startswith('From:'):
                continue
            # Process our 'interesting' line
            print(line)

if __name__ == '__main__':
    main()
