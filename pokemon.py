import json
import time
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
moves = open("./moves.json", encoding="utf8")
data2 = json.load(moves)
language = input("what language would you like to print: english, french, chinese, or japanese?: ").lower()
def print_pokemon():
    for pokemon in data:
        if language in pokemon['name']:
            print(pokemon['name'][language])
        else:
            print ("language not found")
            break
print_pokemon()
def search_pokemon():
    user_input = 0
    while user_input == 0:
        id = int(input("what pokemon would you like to find the name of? print the id: "))
        if 1 > id or 809 < id:
            print ("that is not a valid id, try again")
        else:
            print (data[id-1]['name'][language])
            user_input += 1
search_pokemon()
def pokemon_types():
    type = input ("what type of pokemon would you like to find?: ").capitalize()
    unprinted = True
    while unprinted == True:
        for pokemon in data:
            if type in pokemon['type']:
                print (pokemon['name'][language])
    if type != pokemon['type']:
        print ("that is not a valid type, please try again")
    else:
            unprinted = False
    print ("here are the moves that these pokemon can learn: ")
    time.sleep(1)
    for pokemon in data2:
        if type in pokemon['type']:
            print (f"{pokemon['accuracy']}, {pokemon['ename']}, {pokemon['power']}")
pokemon_types()
def pokemon_search():
    search = input ("what pokemon would you like to find?: ").capitalize()
    matches = [pokemon for pokemon in data if search.lower() in pokemon["name"].lower()]
    for pokemon in data:
        if search in pokemon['name']:
            print (matches)
pokemon_search()

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!