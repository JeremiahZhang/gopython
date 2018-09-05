stuff = list()
stuff.append('Python')
stuff.append('Jeremy')
stuff.sort()
print(stuff)
print(stuff[0])

print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 0))
