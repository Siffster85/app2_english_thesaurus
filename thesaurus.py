import json

data = json.load(open("data.json"))

def lookup(word):
    if word in data:
        return data[word]
    else:
        return "This word doesn't exist within this dictionary. Please try again."

word = input("What word would you like to lookup? ")

print(lookup(word))
