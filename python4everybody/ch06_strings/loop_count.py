# looping and counting
def loop_count():
    word = 'banana'
    count = 0
    for letter in word.lower():
        if letter == 'a':
            count += 1

    print('Count of a:', count)

def count(word, letter):
    total = 0
    for i in word.lower():
        if i == letter:
            total += 1

    return total

def main():
    word = 'I LOVE PYTHON'
    letter = 'o'
    total = count(word, letter)
    print('count of {0} is {1}.'.format(letter, total))

if __name__ == '__main__':
    main()
