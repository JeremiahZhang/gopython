def print_intro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each players is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def get_inputs():
    # Returns the 3 simulation parameters prob_a, prob_b, and n
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))

    return a, b, n

def sim_n_games(n, prob_a, prob_b):
    # simulate n games and return wins_a and wins_b
    wins_a = 0
    wins_b = 0

    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)

        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1

    return wins_a, wins_b

def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, probA, probB)
    print_summary(wins_a, wins_b)
