hours = input("Enter the number of working hours of employee: ")
rate = input("Enter the payment per working hour: ")
payment = float(hours) * float(rate)
extra_payment = (float(hours)-40)*(float(rate)*0.5)

if float(hours)>40:
	print(payment + extra_payment)
else:
	print(payment)