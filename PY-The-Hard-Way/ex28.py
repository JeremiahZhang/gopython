print(True and True) # 1
print(False and True) # 0
print (1 == 1 and 2 == 1) # 0
print("Test" == "Test") # 1
print(1 == 1 or 2 != 1) # 1
print(True and 1 == 1) # 1
print(False and 0 != 0) # 0
print(True or 1 == 1) # 1
print("test" == "testing") # 0
print(1 != 0 and 2 == 1) # 0
print("test" != "testing") # 1
print("test" == 1) # 0
print(not (True and False)) # 1
print(not (1 == 1 and 0 != 1)) # 0
print(not (10 == 1 or 1000 == 1000)) # 0
print(not (1 != 10 or 3 == 4)) # 0
print(not ("testing" == "testing" and "zed" == "cool guy")) # 1
print(1 == 1 and (not ("testing" == 1 or 1 == 0))) # 1
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3))) # 0
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) # 0