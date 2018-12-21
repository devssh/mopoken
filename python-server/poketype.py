class Poketype:
    def __init__(self, name, weaker_types):
        self.name = name
        self.weaker_types = weaker_types

    def __str__(self):
        return self.name + ": [" + ",".join(self.weaker_types) + "]"

    def __repr__(self):
        return self.name + ": [" + ",".join(self.weaker_types) + "]"


type_advantages = {
    "Fire": ["Grass", "Ghost"],
    "Water": ["Fire"],
    "Grass": ["Electric", "Fighting"],
    "Electric": ["Water"],
    "Psychic": ["Ghost"],
    "Ghost": ["Fighting", "Fire", "Electric"],
    "Fighting": ["Electric"]
}

poketypes = {poketype: Poketype(poketype, weaker_types) for poketype, weaker_types in type_advantages.items()}

if __name__ == "__main__":
    print(poketypes)
