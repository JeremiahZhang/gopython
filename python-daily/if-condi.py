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
