largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    try:
        num = int(num)
        if smallest is None: 
            smallest = num
        if largest is None: 
            largest = num
        
        if num < smallest: 
            smallest = num
        if num > largest: 
            largest = num
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
