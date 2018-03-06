#dictionary of foods and their corresponding prices
foods = {"apple": 1, "banana": 2, "bacon": 8, "stogs": 11, "tortillas": 5, "salt": .7}

#print out names of all foods
def displayFoodNames():
	for item in foods:
		print(item + ": $" + str(foods[item]))

#Invoke displayFoodNames function
displayFoodNames()
