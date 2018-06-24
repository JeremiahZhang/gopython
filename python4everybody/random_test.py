import random

for i in range(10):
    x = random.random()
    print(x)

# get the random num betwen 5, 10 including(5, 10)
a = random.randint(5, 10)
print(a)

# choose an element from a sequence at random
t = [1, 2, 4]
choice_t = random.choice(t)
print(choice_t)
