word = "Hello"
print(f"{word:=<20}")
""" 20 characters
word is in the left:
Hello===============
"""
print(f"{word:!>20}")
"""
word is in the right:
!!!!!!!!!!!!!!!Hello
"""

print(f"{word:/^20}")
""" 20 characters
word is in the middle
///////Hello////////"""

# Generalization
align = "<"
fill_char = "*"
width = 25
print(f"{word:{fill_char}{align}{width}}")