# -*- coding: utf-8 -*-

def scan(stuff):

    dir_north = ('direction', 'north')
    dir_south = ('direction', 'south')
    dir_east = ('direction', 'east')
    dir_west = ('direction', 'west')
    sentence = []
    
    words = stuff.split()
    
    for word in words:
        if word in dir_north:
            print "1-north"
            sentence.append(dir_north)
        elif word in dir_south:
            sentence.append(dir_south)
        elif word in dir_east:
            sentence.append(dir_east)
        elif word in dir_west:
            sentence.append(dir_west)
        else:
            word_weild = ('weild', word)
            sentence.append(word_weild)
    
    return sentence