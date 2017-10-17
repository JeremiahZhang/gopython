def move_tower(n, source, dest, temp):
    if n == 1:
        print("Move disk from {} to {}.".format(source, dest))
    else:
        move_tower(n-1, source, temp, dest)
        move_tower(1, source, dest, temp)
        move_tower(n-1, temp, dest, source)

def hanoi(n):
    move_tower(n, "A", "C", "B")

def main():
    n = eval(input("Enter the disk number: "))
    hanoi(n)

if __name__ == '__main__':
    main()
