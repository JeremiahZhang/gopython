"""
objrball.py

Simulation of racquet game.
Illustrates design with objects.
"""

from random import random

class Player:
    """A player keeps track of service probability and score
    """

    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def wins_serve(self):
        return random() <= self.prob

    def inc_score(self):
        self.score += 1

    def get_score(self):
        return self.score

class RBballGame():
    """A RBballGame represents a game in progress. A game has two players
    and keeps track of which one is currently serving.
    """

    def __init__(self, prob_a, prob_b):
        self.player_a = Player(prob_a)
        self.player_b = Player(prob_b)
        self.server = self.player_a # palyer a always serves first

    def play(self):
        while not self.is_over():
            if self.server.wins_serve():
                self.server.inc_score()
            else:
                self.change_server()

    def is_over(self):
        a, b = self.get_scores()
        return a == 15 or b == 15 or \
              (a == 7 and b == 0) or (b == 7 and a == 0)

    def change_server(self):
       if self.server == self.player_a:
           self.server = self.player_b
       else:
           self.server = self.player_a

    def get_scores(self):
        return self.player_a.get_score(), self.player_b.get_score()

class SimStats:
    """ SimStats handles accumulation of statistics across multiple
    (completed) games. This version tracks the wins and shutouts for
    each player.
    """

    def __init__(self):
        self.awins = 0
        self.bwins = 0
        self.ashuts = 0
        self.bshuts = 0

    def update(self, Game):
        a, b = Game.get_scores()
        if a > b:
            self.awins += 1
            if b == 0:
                self.ashuts += 1
        else:
            self.bwins += 1
            if a == 0:
                self.bshuts += 1

    def print_report(self):
        n = self.awins + self.bwins
        print("Summary of {} games:\n".format(n))
        print("             wins (% total)    shutouts (% wins)   ")
        print("-------------------------------------------------")
        self.print_line("A", self.awins, self.ashuts, n)
        self.print_line("B", self.bwins, self.bshuts, n)

    def print_line(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}  ({2:5.1%}) {3:11}  ({4})"

        if wins == 0:
            shut_str = "----"
        else:
            shut_str = "{0:4.1%}".format(float(shuts/wins))

        print(template.format(label, wins, float(wins)/n, shuts, shut_str))

def print_intro():
    print("This program simulates games of racequetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def get_inputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate?"))

    return a, b, n

def main():
    print_intro()

    prob_a, prob_b, n = get_inputs()

    # Play the games
    stats = SimStats()
    for i in range(n):
        the_game = RBballGame(prob_a, prob_b)
        the_game.play()
        stats.update(the_game)

    # Print the results
    stats.print_report()

if __name__ == '__main__':
    main()
