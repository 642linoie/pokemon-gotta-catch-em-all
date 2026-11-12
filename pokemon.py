import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def search_pokemon():
    language = input("what language would you like to print: english, french, chinese, or japanese?: ")
    for pokemon in data:
        if language == 'english':
            print(pokemon['name']['english'])
        if language == 'french':
            print(pokemon['name']['french'])
        if language == 'japanese':
            print(pokemon['name']['japanese'])
        if language == 'chinese':
            print(pokemon['name']['chinese'])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# Add a language choice feature +nd print the pokemons name based on the user input
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file to