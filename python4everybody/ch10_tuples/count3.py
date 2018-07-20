import string
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch09_dictionary/romeo-full.txt'

counts = dict()

with open(fname) as fh:
    for line in fh:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

lst = list()

for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[0:10]:
    print(key, val)
