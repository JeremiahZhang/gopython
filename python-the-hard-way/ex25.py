# -*- coding: utf-8 -*-

"""
本例子可以用来 进行才词频统计
"""

def break_words(stuff): # 拆分句子为单词 list
	"""This function will break up words for us."""
	words = stuff.split(" ") # words type: list $type(words)
	return words # each word in a list named words

def sort_words(words): # 排列单词 字母大小姐
	"""Sorts the words."""
	return sorted(words) # type: list

def print_first_word(words): # 打印第一个单词
	"""Prints the first word after popping it off."""
	word = words.pop(0) # remove item at index 0 返回 words list中第一个单词
	print word

def print_last_word(words): # 打印最后一个单词
	"""Prints the last word after popping it off."""
	word = words.pop(-1) # remove item at index -1 返回 words list中的最后一个单词
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence) # 句子strings --> 变为 包含一个个单词的list
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence) # 拆分句子为单词 list
	print_first_word(words)
	print_last_word(words) 

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence) # 排列单词
	print_first_word(words) # 打印第一个单词
	print_last_word(words) # 打印最后一个单词