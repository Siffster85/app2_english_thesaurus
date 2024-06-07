import json
import difflib

data = json.load(open("data.json"))

def lookup(word):
    lower_word = word.lower()
    if lower_word in data:
        return data[lower_word]
    else:
        suggestion = difflib.get_close_matches(lower_word, data.keys(), n=1)
        if len(suggestion) > 0:
            response = input("This word doesn't exist within this dictionary, did you mean '" + suggestion[0] + "' instead? Enter 'y' if yes or 'n' if no: ")
            if response == "y":
                return data[suggestion[0]]
            if response == 'n':
                return "Please try again."
            return "Your input is invalid, please try again."
        else:
            return "This word doesn't exist within this dictionary, please try again."

word = input("What word would you like to lookup? ")
output = lookup(word)

if type(output) == list:
    for item in output:
        print(item)
else: print (output)
