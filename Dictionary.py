import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead" %get_close_matches(word , data.keys())[0])
        decide = input("Press Y for Yes or N for No : ")
        if decide == "Y" or decide == "y"  :
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "N" or decide == "n":
            return ("Sorry, does not match!")
        else:
            return("Please enter Y or N only! Try again.")
    else:
        return print("Sorry, does not match!")
    

word = input("Enter the word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
