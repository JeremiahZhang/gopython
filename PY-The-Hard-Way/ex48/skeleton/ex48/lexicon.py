# -*- coding: utf-8 -*-

def scan(stuff):

    direction_words = [
        'north', 'south', 'east', 'west',
        'down', 'up', 'left', 'right',
        'back'
        ]

    verbs = ['go', 'stop', 'kill', 'eat']

    sentence = []

    words = stuff.split()

    for word in words:
        if word in direction_words:
            sentence.append(('direction', word))
        elif word in verbs:
            sentence.append(('verb', word))
        else:
            print "Can't recognize %s" % word

    return sentence