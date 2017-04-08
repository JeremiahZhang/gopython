# -*- coding: utf-8 -*-
from ex48.parser import *

# word_list = [
#             ('verb', 'run'), ('direction', 'north'),
#             ('stop', 'the'), ('stop', 'a')
# ]

word_list = [
            ('verb', 'run'),('stop', 'the'),  ('direction', 'north'),
            ('stop', 'a')
]

# word_list = [
#             ('stop', 'the'), ('stop', 'a'),
#             ('verb', 'run'), ('direction', 'north'),
# ]

# x = parse_sentence(word_list)
# print x.subject
# print x.verb
# print x.object
# print x.subject

# print peek(word_list)

# print match(word_list, 'verb')

skip(word_list, 'stop')
print word_list

"""
skip function skip的是在前面的 'word_type' 对应的词

"""