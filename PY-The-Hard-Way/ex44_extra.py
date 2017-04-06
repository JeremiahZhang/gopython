# -*- coding: utf-8 -*-

class Account(object):

	## class definition method
	## Complete Listing of the Account Class

	# constructor
	def __init__(self, holder, number, balance, credit_line=1500):
		# self.Holder = holder ## 可被外部获取 所以需要 Data Encapsulation
		# self.Number = number
		# self.Balance = balance
		# self.CreditLine = credit_line
		self.__Holder = holder
		self.__Number = number
		self.__Balance = balance
		self.__CreditLine = credit_line

	# destructor
	# def __del__(self):
	# 	print "Destructor started."

	# 存钱
	def deposit(self, amount):
		self.__Balance += amount

	# 取钱
	def withdraw(self, amount):
		if (self.__Balance - amount < -self.__CreditLine):
			# 透支额度不足，不能透支啦
			return False
		else:
			self.__Balance -= amount
			return True

	# 账户余额
	def balance(self):
		return self.__Balance

	# 转账
	def transfer(self, target, amount):
		if (self.__Balance - amount < -self.__CreditLine):
			# 转账失败, 信用余额不够
			return False
		else:
			self.__Balance -= amount
			target.__Balance += amount
			return True


# class

""" 

The four major principles of object orientation are: 

1. encapsulation
2. data abstracion
3. polymorphism 多态性 
4. inheritance 

"""

