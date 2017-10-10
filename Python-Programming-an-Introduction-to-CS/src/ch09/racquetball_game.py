def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_games(n, probA, probB)
    print_summary(wins_a, wins_b)
    
