import json
from difflib import get_close_matches, SequenceMatcher


data = json.load(open("data.json"))


def describe(word):

	if word.capitalize() in data:
		return data[word.capitalize()]

	elif word.upper() in data:
		return data[word.upper()]


	word = word.lower()

	if word in data:
		return data[word]
	
	elif get_close_matches(word, data.keys()):

		word_list = get_close_matches(word, data.keys(), 10)

		if len(word_list) == 1:

			yn = input(f"Did you mean {word_list[0]} instead? Enter Y if yes or N if no: ")

			if yn.lower() == "y":
				return data[word_list[0]]

			elif yn.lower() == "n":
				return f"The word '{word}' does not exist."

			else:
				return "I don't unerstand :/"

		else:

			print("I found 10 possible variants: ")

			for index, item in enumerate(word_list, 1):   # word: treeee  -  word_list [tree, treat, tee]

				word_ratio = str(round(SequenceMatcher(None, word, item).ratio(), 4)) + "%"

				print(f"{index}. {item} - {word_ratio}")



			while True:
				opt = input("\nPlease, choose option N: ").strip()

				if not opt.isnumeric():
					print("Please choose correct digit number!")

					continue

				elif int(opt) not in range(1, len(word_list) + 1):
					print("Please choose N in listed range!")

					continue

				opt = int(opt)     # 7 ---> 6
				break


			choosed_word = word_list[opt - 1]

			print(f"Choosed word: {choosed_word}")

			return data[choosed_word]


	else:
		return "The entered word does not exist."


def format_output(output):

	if type(output) == str:
		print(output)

	elif len(output) == 1:
		print(output[0])

	else:
		for index, item in enumerate(output, 1):
			print(f"{index}. {item}")


while True:

	word = input("\nEnter the word or type 'exit': ")

	if word == "exit":
		print("Bye bye!")
		break

	format_output(describe(word))