hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate:")
rate= float(rate)
rate2 = 1.5 * rate
pay = 0

if h > 40:
    pay = 40 * rate + (h - 40) * rate2
else:
    pay = h * rate

print(pay)
