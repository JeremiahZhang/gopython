class TextInterface:

    def __init__(self):
        print("Welcome to video poker.")

    def set_money(self, amt):
        print("You currnetly have ${}".format(amt))

    def set_dice(self, values):
        print("Dice:", values)

    def want_to_play(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in "yY"

    def close(self):
        print("\nThanks for you playing")

    def show_result(self, msg, score):
        print("{0}. You win ${1}".format(msg, score))

    def chose_dice(self):
        return eval(input("Enter list of which to change ([] to stop) "))
