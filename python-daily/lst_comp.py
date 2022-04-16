product_prices = {
	"bread": 0.2, "chocolate": 1,
	"book": 20, "car": 20000,
}

expensive = []
for product, price in product_prices.items():
	if price > 100:
		expensive.append(product)

expensive_lst = [product for product, price in product_prices.items() if price > 100]

print(expensive)
print("list comprehension")
print(expensive_lst)