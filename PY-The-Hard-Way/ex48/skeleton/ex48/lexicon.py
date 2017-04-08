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
            try:
                num = int(word)
                sentence.append(('number', num))
            except ValueError:
                print "Plest input correctly."

    return sentence
