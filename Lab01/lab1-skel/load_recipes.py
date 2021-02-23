"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""

RECIPES_FOLDER = "recipes"
# dictionar in care retin reteta pentru fiecare cafea data la input
utilities = {}

ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

def load(coffeeType):

	if coffeeType == AMERICANO:
		file = 'recipes/americano.txt'
	elif coffeeType == CAPPUCCINO:
		file = 'recipes/cappuccino.txt'
	elif coffeeType == ESPRESSO:
		file = 'recipes/espresso.txt'

	with open(file, 'r') as f:
		idx = 0
		for line in f:
			if line.rstrip() != coffeeType:
				utilities[idx] = int(line.split("=")[1])
				idx += 1
