def main():
    count = 0
    total = 0
    avg = 0
    while True:
        number = input("Enter a num: ")
        if number == 'done':
            break

        try:
            number = int(number)
            count += 1
            total += number
        except:
            print('Invalid input.')

    avg = total / count
    print('Sum: ', total)
    print('Count: ', count)
    print('Average: ', avg)

if __name__ == '__main__':
    main()
