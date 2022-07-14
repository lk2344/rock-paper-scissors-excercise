game.py
#this is the "game.py" file...

print("Welcome to my Rock, Paper, Scissors Game")


#process user inputs

user_input = input("Please choose one ('rock', 'paper', 'scisors'")

print("You chose:", user_input)


#Validate user inputs


#simulate computer selection

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)


#determine winner

if user_input == "rock":
	if computer_choice == "rock":
		print("TIE")
	elif computer_choice == "paper":
		print("You Lost :(")
	elif computer_choice == "scissors":
		print("You Win!")
elif user_input == "paper":
	if computer_choice == "paper":
		print("TIE")
	elif computer_choice == "scissors":
		print("You Lost :(")
	elif computer_choice == "rock":
		print("You Win!")
elif user_input == "scissors":
	if computer_choice == "scissors":
		print("TIE")
	elif computer_choice == "rock":
		print("You Lost :(")
	elif computer_choice == "paper"
		print("You Win!")										


#display result


