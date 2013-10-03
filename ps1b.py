
# Problem Set 1
# Name: Kevin Wang
# Time Spent: 1:00


# Problem 2 - Paying off in a year

# Write a program to calculate the credit card balance after one 
# year if a person only pays the minimum monthly payment required 
# by the credit card company each month

balance = input("What is the outstanding balance on the credit card? ")
rate = input("What is the annual interest rate? ")

payment = 10

def calculate():
	total_payment = 0
	b = float(balance)
	for x in range(1,13):
		new_balance = float(b) * (1 + (float(rate) / 12)) - payment
		print(" ")
		print(new_balance)
		total_payment += payment
		print(total_payment)
		b = new_balance
	return new_balance

nb = calculate()

def check():
	if nb > 0:
		print("FALSE")
		payment += 10
		calculate()
		check()
	else:
		return True	

check()

# if nb > 0:
# 	payment +=10
# 	calculate()
# else:	
# 	print("\nRESULT")
# 	print("Monthly payment to pay off debt in 1 year: " + str(months))
# 	print("Balance: " + str(balance))
