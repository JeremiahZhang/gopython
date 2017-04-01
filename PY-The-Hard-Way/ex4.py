# -*- coding: utf-8 -*-

cars = 100   			# 轿车总数
space_in_a_car = 4.0	# 每辆轿车可坐人数, 这里是float
drivers = 30			# 司机数目								
passengers = 90			# 乘客数目
cars_not_driven = cars - drivers # 不能被用起来的轿车数目=轿车总数-司机数
cars_driven = drivers	# 一个司机开一辆车, 就有多少车被用起来
carpool_capacity = cars_driven * space_in_a_car # 现有的总承载能力
average_passengers_per_car = passengers / cars_driven # 平均承载能力

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

"""

1. variables 变量赋值
2. space_in_a_car 变量命名
3. =
4. _
5. x = 100 比 x=10 跟容易读。 易读性
6. read the file backward 倒读代码

"""