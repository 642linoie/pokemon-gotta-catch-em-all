import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
language = input("what language would you like to print: english, french, chinese, or japanese?: ")
def print_pokemon():
    for pokemon in data:
        if language in pokemon['name']:
            print(pokemon['name'][language])
        else:
            print ("language not found")
            break
print_pokemon()
def search_pokemon():
    id = int(input("what pokemon would you like to find the name of? print the id: "))
    print (data[id-1]['name'][language])
search_pokemon()
def pokemon_types():
    type = input ("what type of pokemon would you like to find?")
    for pokemon in data:
        if type in pokemon['type']:
            print (pokemon['name'][language])
pokemon_types()
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file to