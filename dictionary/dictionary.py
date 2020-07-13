import json
from difflib import get_close_matches
x = 'y'

def meaning(key):
    key = key.lower()
    if key in data.keys():
        print(data[key][0])
    elif key.upper() in data.keys() :
        print(data[key.upper()][0])
    elif key.title() in data.keys() :
        print(data[key.title()][0])
    elif key not in data.keys():
        closer_match = get_close_matches(key,data.keys())[0]
        print(f"Did you mean :- {closer_match}")
        yn = input('If yes enter y :- ')
        if(yn=='y'):
            print(data[closer_match][0])
        else:
            print(f"{key} is not in the dictionary")

if __name__ ==  "__main__":
    data = json.load(open('data.json'))
    while(x == 'y'):
        key = input('Enter Word to be searched: ')
        meaning(key)
        x = input('Enter y to search more:- ')
