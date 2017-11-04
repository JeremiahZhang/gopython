def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg

    print "-" * 40

    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

def main():
    print(0)
    parrot(1000)                                          # 1 positional argument
    print(1)
    parrot(voltage=1000)                                  # 1 keyword argument
    print(2)
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    print(3)
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    print(4)
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    print(5)
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

if __name__ == '__main__':
    # main()
    cheeseshop("Limburge", "It's very runny, sir",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")
