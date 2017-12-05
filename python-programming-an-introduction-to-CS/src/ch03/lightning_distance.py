# lightning_distance.py
#   A program that determines the distance to a lightning
#   strike based on the time elapsed between the flash and
#   the sound of thunder.

def main():
    print("Please enter the time elapsed between")
    print("the flash and the sound of thunder.")
    print()

    elapsed_time = eval(input("Please enter: "))

    distance = 1100 / 5280 * elapsed_time

    print("The lightning distance is approximating {} miles.".format(distance))

main()
