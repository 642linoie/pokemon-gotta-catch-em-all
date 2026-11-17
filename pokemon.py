import json
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
    type = input ("what type of pokemon would you like to find?")
    for pokemon in data:
        if type in pokemon['type']:
            print (pokemon['name'][language])
pokemon_types()
def name_finding():
    name = input("what pokemon would you like to find?: ")
     
def pokemon_moves():
    types = input("what type of moves would you like to find?: ")
    for pokemon in data2:
        if types in pokemon['type']:
            print (pokemon['accuracy'], ['ename'], ['power'])
pokemon_moves()
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file to