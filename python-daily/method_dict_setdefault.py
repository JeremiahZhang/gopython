"""
dictionary.setdefault(keyname, value)
"""

car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

# color of car is white
x = car.setdefault("color", "white")
print(x)
print(car)

# price of the car
x = car.setdefault("price", []).append((19000, 23000))
print(x)
print(car)

# type of the car
x = car.setdefault("type", [("auto", "manual")])
print(x)
print(car)