sentence = input("sentence:>>>")

items = [x.upper() for x in sentence.split(' ')]

print(' '.join(items))

# or
print("Or")
print(sentence.upper())