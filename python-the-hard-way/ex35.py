# -*- coding: utf-8 -*-

from sys import exit

def gold_room(): # function 定义
    print "This room is full of gold. How much do you take?"
    
    choice = raw_input("> ") # 交互 键入
    
    if "0" in choice or "1" in choice: # 输入是否是数字 这个不怎么好 如果是2 就不行了 必须有0 or 1才行要不就 跳到 line 13
        how_much = int(choice) # 转化为数字
    else:
        dead("Man, learn to type a number.")

    if how_much <= 50: # 键入数字是否小于等于50 是则不怎么贪婪 若大于 50 则表示太贪婪
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room(): # if left then 进入 bear_room 
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?(take honey? taunt bear? or open door?"
    bear_moved = False # the bear has not been moved if it is False

    while True: # 下面有跳出 while 的function 可以跳出while loop 避免死循环
        choice = raw_input(">")  # 交互：输入 “take honey” 或 “taunt bear” 或其他
        
        if choice == "take honey": # 输入 take honey 则进入 dead funciton
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved: # 输入 taunt bear 而且 bear 还没被移开则 打印 下面 
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True # 并 移开熊 再回到 while Ture 进入while loop
        elif choice == "taunt bear" and bear_moved: # 如果 taunt bear 键入 而且 bear_moved = True
            dead("the bear get pissed off and chews your leg off.") # 则进入 dead function
        elif choice == "open door" and bear_moved: # 如果 键入 open door 并且 bear_moved = True
            gold_room() # 则进入 黄金屋子
        else: # 以上都不是 则再次进入 此 while loop 直到可以 跳出 该 loop
            print "I got no idea what that means."
    
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you going insane."
    print "Do you flee for your life or eat your head?"
    
    choice = raw_input("flee or head> ")
        
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def dead(why): # why 是提示说明
    print why, "Good job!"
    exit(0)                 # 退出程序

def start():
    print "You are in a dark room."
    print "Ther is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")
    
    if choice == "left": # 如果输入 left 则进入 bear_room function
        bear_room()
    elif choice == "right": # 如果输入 right 则进入 cthulhu_room function
        cthulhu_room()
    else:   # 都不是, 则进入 dead function
        dead("You stumble around the room until you starve.")

start() # 开始 start function