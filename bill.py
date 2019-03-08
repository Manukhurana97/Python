names = ['A', 'B', 'C', 'D', 'E']
bills = ['100.1', '124.6', '411', '67.77', '220']
message = '''
	Hello {name} .
	Your total amount is {bill}
	
	Thanks for shopping .

	welcome again 
'''


def send_message(customer, amount):
	i = 0
	if len(customer) == len(amount):
		for each_customer in customer:
			new_message = message.format(name = each_customer, bill=amount[i])
			i += 1
			print(new_message)
	else:
		print('no amount for the customers')


send_message(names, bills)

ZZ = dict(zip(names, bills))
print(ZZ)