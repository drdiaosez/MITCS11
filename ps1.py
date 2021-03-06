
# Problem Set 1
# Name: Kevin Wang
# Time Spent: 3:00

# Write a program to calculate the credit card balance 
# after one year if a person only pays the minimum monthly 
# payment required by the credit card company each month

# Minimum Monthly Payment
# Interest Paid
# Principal Paid
# Remaining Balance

balance = input("What is the outstanding blance on the credit card? ")
rate = input("What is the annual interest rate? ")
payment_rate = input("What is the minimum monthly payment rate? ")

# Print minimum monthly payment
# Print remaining balance
# Print principle

principle_paid = 0
total_paid = 0

for x in range(1, 13):
	print("\nMonth = " + str(x))

	minimum_monthly_payment = float(balance) * float(payment_rate)
	interest_paid = (float(rate) / 12) * float(balance)
	principle_paid = float(minimum_monthly_payment) - float(interest_paid)
	remaining_balance = float(balance) - float(principle_paid)

	mmp = int(minimum_monthly_payment * 100) / 100.0
	pp = int(principle_paid * 100) / 100.0
	rb = int(remaining_balance * 100) / 100.0

	total_paid += minimum_monthly_payment
	tp = int(total_paid * 100) / 100.0

	print("Minimum monthly payment = " + str(mmp))
	print("Principle paid = " + str(pp))
	print("Remaining balance = " + str(rb))

	balance = remaining_balance

print("\nRESULT")
print("Total Amount Paid = " + str(tp))
print("Remaining balance = " + str(rb))
