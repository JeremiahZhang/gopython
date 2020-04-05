txt = "Company X I love Python Python"

words_list = txt.split()

words_dict = {}

for word in words_list:
    if word not in words_dict.keys():
      words_dict[word] = 1
    else:
      words_dict[word] += 1

print(words_dict)
