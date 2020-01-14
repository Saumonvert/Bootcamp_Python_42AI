import random

def guessthenumber():
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!\n")
	nb = random.randint(1,99)
	i = 0
	while (1):
		print("What's your guess between 1 and 99?")
		option = input()
		i += 1
		if option == "exit":
			exit("Goodbye!")
		elif not option.isnumeric():
			print("That's not a number.")
		elif int(option) > nb:
			print("Too high!")
		elif int(option) < nb:
			print("Too low!")
		elif int(option) == nb:
			ggmsg = "You won in {} attempts!"
			if nb == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if i == 1:
				exit("Congratulations, you've got it on your first try!")
			print("Congratulations, you've got it!")
			exit(ggmsg.format(i))
		
guessthenumber()