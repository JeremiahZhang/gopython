points = 174  # use this input to make your submission

# write your if statement here
result = ""

if points >= 1 and points <= 50:
    result = "Congradulations! You won a {0}!".format("wooden rabbit!")
elif points >= 51 and points <= 150 :
    result = "Oh dear, {} this time.".format("no prize")
elif points >= 151 and points <= 180:
    result = "Congratulations! You won a {0}!".format("wafer-thin mint")
else:
    result = "Congradulations! You won a [{0}!".format("penguin")


print(result)

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 5 #provide answer
guess = 9 #provide guess

if guess < answer:#provide conditional
    result = "Oops!  Your guess was too low."
elif guess > answer: #provide conditional
    result = "Oops!  Your guess was too high."
elif guess == answer: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)

# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "CA" #Either CA, MN, or NY
purchase_amount = 100 #amount of purchase

if state == "CA": #provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == "MN": #provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == "NY": #provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
