import sys

res = sys.argv[1]
res2 = sys.argv[2]
lst = ["1", "2"]

if len(sys.argv) > 3:
	print("InputError: too many arguments")
elif type(res) != str or res2.isnumeric() == False:
	print("ERROR")
else:
	a1 = res.split()
	a2 = int(res2)
	for x in a1:	
		if len(x) > a2:
			lst.append(x)
	lst.pop(0)
	lst.pop(0)
	print(lst)