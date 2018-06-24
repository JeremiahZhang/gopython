def main():
    word = input('Enter a word: ')
    word = word.lower()
    if word == 'banana':
        print('All right, bananas.')
    elif word < 'banana':
        print('You word, ' + word + ', comes before banana.')
    else:
        print('You word, ' + word + ', comes after banana.')

if __name__ == '__main__':
    main()
