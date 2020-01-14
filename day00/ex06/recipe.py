import subprocess

cookbook = {'sandwich': {'meal': 'lunch', 'prep_time': '10'},
			'cake': {'meal': 'dessert', 'prep_time': '60'},
			'salad': {'meal': 'lunch', 'prep_time': '15'}}
cookbook['sandwich']["ingredients"] = ["ham", "bread", "cheese", "tomatoes"]
cookbook['cake']["ingredients"] = ["flour", "sugar", "eggs"]
cookbook['salad']["ingredients"] = ["avocado", "arugula", "tomatoes", "spinach"]

def printrecipe(recipename):
	one = "Recipe for " + recipename + ":"
	print(one)
	#--------------#
	print("Ingredients list: ", end="")
	print(cookbook[recipename]['ingredients'])
	#--------------#
	print("To be eaten for " + cookbook[recipename]['meal'] + ".")
	#--------------#
	two = "Takes {} minutes of cooking."
	print(two.format(cookbook[recipename]['prep_time']))

def delrecipe(recipename):
	del cookbook[recipename]

def addrecipe(name, item1, item2, item3):
    if name in cookbook:
        print("This recipe is already in the book.")
    else:
        cookbook[name] = dict(ingredients=item1, meal=item2, prep_time=item3)

def printbook():
	print("Recipes:")
	for x in cookbook:
		print("• " + x)

def printmainmenu():
	print("\n •---------------• \n")
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def book():
	printmainmenu()
	while (1):
		print("\n •---------------• \n")
		option = input()
		if option == 'm':
			subprocess.call(['clear'])
			printmainmenu()
		elif option == '1':
			option1_n = input("Please enter your recipe's name: ")
			option1_i = input("List the ingredients in this format please [\"ingredient1\", \"ingredient2\"] : ")
			option1_m = input("Your meal should be eaten for: ")
			option1_t = input("How long will it take to prep your meal ? (in minutes) ")
			subprocess.call(['clear'])
			addrecipe(option1_n, option1_i, option1_m, option1_t)
			printmainmenu()
		elif option == '2':
			option2 = input("Please enter the recipe's name to delete it: ")
			subprocess.call(['clear'])
			delrecipe(option2)
			print("\n •---------------• \n")
			print(option2 + " deleted.")
		elif option == '3':
			option3 = input("Please enter the recipe's name to get its details: ")
			subprocess.call(['clear'])
			print("\n •---------------• \n")
			printrecipe(option3)
		elif option == '4':
			subprocess.call(['clear'])
			print("\n •---------------• \n")
			printbook()
		elif option == '5':
			subprocess.call(['clear'])
			print("Cookbook closed.")
			return
		else:
			print("\n •---------------• \n")
			print("This option does not exist, please type the corresponding number.")
			print("To exit, enter 5.")

book()