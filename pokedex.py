from helper.writeAJson import writeAJson
from main import db


def getPokemonByName(name: str):
    return db.collection.find({"name": name})
ratata = getPokemonByName("Ratata")
writeAJson(ratata, "Ratata")


def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})
types = ["Fire"]
pokemons_fire = getPokemonsByType(types)
writeAJson(pokemons_fire, "pokemonsDeFogo")



pokemons_ice_andorweak = db.collection.find({"$or": [{"type":"Ice"},{"weaknesses": "Ice"}]})
writeAJson(pokemons_ice_andorweak, "pokemonsFracosContraOuDeGelo")


pokemons_chance = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(pokemons_chance, "pokemonsChanceDeSpawn")



pokemons_Nomultiplier = db.collection.find({"multipliers": {"$exists": False}})
writeAJson(pokemons_chance, "pokemonsSemMultiplicador")