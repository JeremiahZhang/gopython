file = input('Enter file:')
diff_words = []

with open(file) as f:
    for line in f:
        words = line.split()
        if len(words) > 0:
            for word in words:
                if word in diff_words:
                    continue
                else:
                    diff_words.append(word)

    diff_words.sort()
    print(diff_words)
            
