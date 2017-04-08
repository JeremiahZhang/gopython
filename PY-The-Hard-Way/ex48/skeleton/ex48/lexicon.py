# -*- coding: utf-8 -*-

def scan(stuff):

    direction_words = [
        'north', 'south', 'east', 'west',
        'down', 'up', 'left', 'right',
        'back'
        ]

    sentence = []

    words = stuff.split()

    for word in words:
        if word in direction_words:
            sentence.append(('direction', word))
        else:
            print "%s is not a direction" % word

    return sentence