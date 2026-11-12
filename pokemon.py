import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
language = input("what language would you like to print: english, french, chinese, or japanese?: ")
def print_pokemon():
    for pokemon in data:
        if language in pokemon['name']:
            print(pokemon['name'][language])
        else:
            print("invalid language given")
print_pokemon()
def search_pokemon():
    pokemon = int(input("what pokemon would you like to find the name of? print the id: "))
    if id in (data):
        print (pokemon['id']['name'][language])
    else:
        print ("invalid id")
search_pokemon()
# Add a language choice feature +nd print the pokemons name based on the user input
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file to