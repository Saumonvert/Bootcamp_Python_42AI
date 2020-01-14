import sys

res = sys.argv[1]
res2 = sys.argv[2]

if len(sys.argv) > 3:
	print("InputError: too many arguments")
elif res.isnumeric() and res2.isnumeric():
	arg1 = int(sys.argv[1])
	arg2 = int(sys.argv[2])

	res1 = arg1 + arg2
	sumtxt = "Sum:      {}"
	print(sumtxt.format(res1))
	#----------------#
	res2 = arg1 - arg2
	difftxt = "Difference: {}"
	print(difftxt.format(res2))
	#----------------#
	res3 = arg1 * arg2
	prodtxt = "Product: {}"
	print(prodtxt.format(res3))
	#----------------#
	if arg1 and arg2:
		res4 = arg1 / arg2
		quottxt = "Quotient: {}"
		print(quottxt.format(res4))
	else:
		print("Quotient: ERROR (div by zero)")
	#----------------#
	if arg1 and arg2:
		res5 = arg1 % arg2
		remtxt = "Remainder: {}"
		print(remtxt.format(res5))
	else:
		print("Remainder: ERROR (modulo by zero)")
else:
	print("InputError: only numbers")