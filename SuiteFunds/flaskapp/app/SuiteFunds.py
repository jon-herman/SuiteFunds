######################################################################
# Jonathan Herman
# 
# SuiteFunds
#	The SuiteFunds class takes a dictionary of debts and balances it.  
#
######################################################################

def main():
	''' Tester for SuiteFunds class '''

	# Dictionary with pairs: (Name, amount owed)
	funds = {"David": -5,
			"Jason_A" : 15,
			"Jason E" : 26,
			"Jon": 26,
			"Eitan": -39,
			"Dylan": -46,
			"Gabe": 26,
			}
	# payments is a string that will record the necessary payments
	payments = []
	# Threshold is the error due to rounding
	threshold = 5
	payments = getPayments(funds, payments, threshold)

	return payments

def getFunds(input):
	''' Takes payments as input and outputs funds dictionary'''

	data = input.split()
	# Initialize funds dictionary
	funds = {"David": 0, "Jason_A": 0, "Jason E": 0, "Jon": 0, "Eitan": 0, "Dylan": 0, "Gabe": 0}

	# Fill dictionary values
	for i in range(0,len(data),2):
		name = data[i]
		''' Handle exception thrown when an invalid name is inserted '''
		cost = int(data[i+1][1:])
		funds[name] -= cost

		# This could be used to generalize the app beyond the suite:
		'''
		# If the name is in the dictionary, update it...
		if name in funds.keys():
			funds[name] -= cost
			
		# If not, add it
		else:
			funds[name] = -cost
		'''

	print(funds)
	members = 7.0
	perPerson = round( sum(funds.values()) / members )

	# Add perPerson to each member
	for key in funds.keys():
		funds[key] += abs(perPerson)

	return funds


def getPayments(funds, payments, threshold):
	i = 0;
	while(max(funds.values()) >= threshold):
		''' Would be faster to put all the keys in a heap '''
		for name in funds:
			if(funds[name] > 0):
				debt = funds[name]
				# OWED is who is owed to; CREDIT is the amount owed
				(owed, credit) = getMinPair(funds)
				# name pays either as much as they owe, or as mouch as min is owed
				payment = min(debt, abs(credit))
				makePayment(funds, name, owed, payment)

				# Add payment to output
				payments.append(str(name) + " pays " + str(owed) + " $" + str(payment))

		# Error Check: break infinite loops
		if i > 10:
			# Clear output and display message
			payments = []
			payments.append("Invalid input. Make sure values sum to zero and try again!")

			return payments
		i += 1

	# Report rounding error
	(maxKey, maxVal) = getMaxPair(funds)
	payments.append(maxKey + " buys the suite $" + str(maxVal) + " worth of ice cream!")

	return payments


def getMinPair(funds):
	''' Gets the person owed the most, and what he is owed '''

	minKey = 'David'
	minVal = funds[minKey]
	for name in funds:
		if funds[name] < minVal:
			minVal = funds[name]
			minKey = name

	return (minKey, minVal)

def getMaxPair(funds):
	maxKey = 'David'
	maxVal = funds[maxKey]
	for name in funds:
		if funds[name] > maxVal:
			maxVal = funds[name]
			maxKey = name

	return (maxKey, maxVal)

def makePayment(funds, source, target, payment):
	''' Applies payment '''

	funds[source] -= payment
	funds[target] += payment


# Call main()
# main()
