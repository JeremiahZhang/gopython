# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# dict
PHRASES = { \
	"class %%%(%%%):": \
		"Make a class named %%% that is-a %%%.", \
	"class %%%(object): \n\tdef __init__(self, ***)": \
		"classs %%% has-a __init__ that takes self and *** parameters.", \
	"class %%%(object): \n\tdef ***(self, @@@)": \
		"class %%% has-a function named *** that takes self and @@@ parameters.", \
	"*** = %%%()":\
		"Set *** to an instance of class %%%.", \
	"***.***(@@@)": \
		"From *** get *** function, and call it with paraters self, @@@.", \
	"***.*** = '***'": \
		"From *** get the *** attribute and set it to '***'."}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
else:
	PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet, phrase):
	print "this snippet key is: ", snippet
	print "this phrase relate to snippet key is: ", phrase

	class_names = [w.capitalize() for w in \
					random.sample(WORDS, snippet.count("%%%"))] # sample a k(snippet.count("%%%")) length list of unique elements chosen from WORDS list 
	print "class_names is ", class_names

	other_names = random.sample(WORDS, snippet.count("***"))
	print "other_names is ", other_names

	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3) # return a random integer N such that 1<= N <=3
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		print "param_names is: ", param_names

	for sentence in snippet, phrase: # for x in y, then for x in z
		result = sentence[:] # 
		print "1-st result:", result

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
			print "2nd result:", result

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			print "3rd result:", result

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			print "4th result:", result

		results.append(result)

	print results	

	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys() # PHRASES key
		print "The key is: ", snippets

		random.shuffle(snippets) # randomize these keys
		print "the shuffled key is: ", snippets

		for snippet in snippets: # snippet is one key in PHRASES
			phrase = PHRASES[snippet] # value of the key in PHRASEs dict
			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBYE"