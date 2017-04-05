# -*- coding: utf-8 -*-

# modules are like dictionaries

# classes are like modules

# objects are like import

""" 
instantiate == create

# dict style
mystuff = {'apple': "I am apples!"}
print mystuff['apples']

---

# module style
## this goes in mystuff.py
def apple():
	print "I am apples!"
tangerine = "Living reflection of a dream" # just a variable

import mystuff

mystuff.apples()
print mystuff.tangerine

---

# class style

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print "I am class apples!"

thing = MyStuff() # instantiate a class == creat a class
thing.apples()
print thing.tangerine

"""

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def creat_a_song(self):
		print "I love you, my lover!"

happy_bday = Song(["Happy birthday to you", \
					"I don't want to get sued", \
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", \
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# study drill
print "-" * 10

sunny_day = ["It's a sunny day", "We love to travlling"]
song_of_sunny_day = Song(sunny_day)

song_of_sunny_day.sing_me_a_song()

print "-" * 20
song_of_sunny_day.creat_a_song()