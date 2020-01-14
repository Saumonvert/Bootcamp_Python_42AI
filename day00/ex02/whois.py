import sys

args = ' '.join(sys.argv[1:])

if args.isnumeric():
	nb = int(sys.argv[1])
	if nb == 0:
		print("I'm Zero.")
	elif nb % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
elif args[0] == '-':
	if args[1:].isnumeric():
		nb = int(sys.argv[1])
		if nb == 0:
			print("I'm Zero.")
		elif nb % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	else:
		print("ERROR")
else:
	print("ERROR")