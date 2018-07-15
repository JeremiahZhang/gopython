import re

counts = dict()
print('Enter a line of text: ')
line = input('')
line = line.lower()

words = re.split(r'\W+', line)

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)
