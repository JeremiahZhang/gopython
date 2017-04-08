# -*- coding: utf-8 -*-

def scan(stuff):

    direction_words = [
        'north', 'south', 'east', 'west',
        'down', 'up', 'left', 'right',
        'back'
        ]

    verbs = ['go', 'stop', 'kill', 'eat']

    stop_words = [
        'the', 'in', 'of',
        'from', 'at', 'it'
        ]

    nouns = ['door', 'bear', 'princess', 'cabinet']

    numbers = [i for i in range(0, 10)]

    sentence = []

    words = stuff.split()

    for word in words:
        if word in direction_words:
            sentence.append(('direction', word))
        elif word in verbs:
            sentence.append(('verb', word))
        elif word in stop_words:
            sentence.append(('stop', word))
        elif word in nouns:
            sentence.append(('noun', word))
        else:
            print "Can't recognize %s" % word

    return sentence