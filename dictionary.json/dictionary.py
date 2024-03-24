import json
import difflib

#function to load the content of the josn file into a python dictionary
def load_dictionary():
    with open('dictionary.json', 'r') as file:
        data = json.load(file)
    return data

dictionary = load_dictionary()

#function to access the definition of a word from the json file
def get_definition(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return None
    
#function to take user input and convert it to lower case   
def get_user_input():
    user_input = input("Please enter a word: ")
    return user_input.lower()

# implement the suggestion mechanism for mispelled words
def suggest_word(word):
    closest_match = difflib.get_close_matches(word, dictionary.keys(), n=1)
    if closest_match:
        return closest_match[0]
    else:
        return None

#main program
def main():
    while True:
        word = get_user_input()
        definition = get_definition(word)
        if definition:
            print(f"Definition: {definition}")
        else:
            suggested_word = suggest_word(word)
            if suggested_word:
                print(f"Word not found.Did you mean '{suggested_word}'?")
            else:
                print("word not found in the dictionary.")

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes' :
            break

if __name__ == "__main__":
    main()
            
        