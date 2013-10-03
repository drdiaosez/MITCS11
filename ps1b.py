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



#=================================================
#
#		Evan's code
#
#=================================================



# Minimum monthly payment = Minimum monthly payment rate x Balance 
# (Minimum monthly payment gets split into interest paid and principal paid) 
# Interest Paid = Annual interest rate / 12 months x Balance 
# Principal paid = Minimum monthly payment – Interest paid 
# Remaining balance = Balance – Principal paid 

# For month 1, we can compute the minimum monthly payment by taking 2% of the balance: 
# Minimum monthly payment = .02 x $5000.0 = $100.0 

# We can’t simply deduct this from the balance because there is compounding interest. Of this 
# $100 monthly payment, compute how much will go to paying off interest and how much will go 
# to paying off the principal. Remember that it’s the annual interest rate that is given, so we need 
# to divide it by 12 to get the monthly interest rate. 
# Interest paid = .18/12.0 x $5000.0 = $75.0 
# Principal paid = $100.0 – $75.0 = $25 

# The remaining balance at the end of the first month will be the principal paid this month 
# subtracted from the balance at the start of the month. 
# Remaining balance = $5000.0 – $25.0 = $4975.0 


#=======================================================
# Enter the outstanding balance on your credit card: 4800 
# Enter the annual credit card interest rate as a decimal: .2 
# Enter the minimum monthly payment rate as a decimal: .04 
# Month: 1 
# Minimum monthly payment: $192.0 
# Principle paid: $112.0 
# Remaining balance: $4688.0 
# Month: 2 
# Minimum monthly payment: $187.52 
# Principle paid: $109.39 
# Remaining balance: $4578.61
# RESULT 
# Total amount paid: $2030.15 
# Remaining balance: $3615.74 


#==========================================
#
#		inputs
#
#==========================================

initBalance = input("Enter the outstanding balance on your credit card: ")
annualRate = input("Enter the annual credit card interest rate as a decimal: ")
minPayRate = input("Enter the minimum monthly payment rate as a decimal: ")

#==========================================
#
#		functions
#
#==========================================

#to do recursion, you call a function within itself. in order to do this, you need to have inputs that are
# different each time the function is called. 
# the changing inputs i added to my function are 'startMonth' and 'totalPaid'
# 'startMonth' increments by 1 each time the function is called
# 'totalPaid' just adds the previous total and the newest payment

#Also, its good to make all ur functions as robust as possible. while the problem specifically asks for u
# to calculate the interest after 12 months, you shud always strive to make ur code be able to accept any number of months.
# I therefore added 'endMonth' as an input as well. 

#"the problem asks for interest after 12 months only doe! and the only inputs can only be the initial balance, 
# annual interest rate, and the minimum payment rate," you say.
# thats fine, i therefore added a wrapper function called 'calculateAnnual'
# more comments for that when you get there


def calculate(initBalance, annualRate, minPayRate, totalPaid, startMonth, endMonth) :
	# for the first call, totalPaid is 0, startMonth is 0, and endMonth is 12
	
	#increment startMonth by 1 each time the function is called
	startMonth += 1 
	
	# i just used the equations given by the prompt. also, used round to make sure everything was only 
	# two decimal points
	minMonthlyPayment = round(minPayRate * initBalance,2)
	interestPaid =  round(annualRate/12 * initBalance,2)
	principlePaid = round(minMonthlyPayment - interestPaid,2)
	newBalance = round(initBalance - principlePaid,2)
	totalPaid += minMonthlyPayment
	
	# nothing interesting here. just outputting based on what was asked for in the prompt
	print('Month:', startMonth)
	print('Minimum monthly payment:', minMonthlyPayment)
	print('Principle paid:', principlePaid)
	print('Remaining balance:', newBalance)
	
	#recursion part
	# as long as startMonth is smaller than endMonth, we recurse. 
	#once startMonth is equal to endMonth, we print the stuff required by the prompt and exit
	if startMonth < endMonth: 
		return calculate(newBalance, annualRate, minPayRate, totalPaid, startMonth, endMonth)
	else: 
		print('RESULT')
		print('Total amount paid:', totalPaid)
		print('Remaining balance:', newBalance)
		return None

#'calculateAnnual' is just a wrapper function that calls 'calculate' except that it only has 3 inputs.
# the other 3 inputs are defined within 'calculateAnnual' so that your code still meets the specs asked for
def calculateAnnual(initBalance, annualRate, minPayRate) :
	totalPaid = 0
	startMonth = 0
	endMonth = 12
	return calculate(float(initBalance), float(annualRate), float(minPayRate), totalPaid, startMonth, endMonth)


#==========================================
#
#		Main
#
#==========================================


calculateAnnual(initBalance, annualRate, minPayRate)
