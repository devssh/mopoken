from poketype import poketypes

advantage_types = {1: "Advantage", 0: "Draw", -1: "Disadvantage"}


class Pokemon:

    def __init__(self, type, level):
        if type not in list(poketypes.keys()):
            raise ValueError("Unknown type of pokemon: " + str(type))
        try:
            if not isinstance(int(level), int):
                raise ValueError("Level of pokemon is not a number: " + str(level))
        except:
            raise ValueError("Level of pokemon is not a number: " + str(level))
        self.type = type
        self.level = level

    def __str__(self):
        return self.type + "#" + str(self.level)

    def __repr__(self):
        return self.type + "#" + str(self.level)

    def __gt__(self, other):
        if self.level > other.level * 2:
            return True
        if (self.level * 2 > other.level) and (other.type in poketypes[self.type].weaker_types):
            return True
        if (self.level > other.level) and (self.type not in poketypes[other.type].weaker_types):
            return True
        return False

    def advantage(self, other):
        def advantage_value(self, other):
            if self > other:
                return 1
            else:
                if other > self:
                    return -1
                else:
                    return 0

        return advantage_types[advantage_value(self, other)]


if __name__ == '__main__':
    print(Pokemon("Fire", 23).advantage(Pokemon("Water", 22)))
    print(Pokemon("Fire", 44).advantage(Pokemon("Water", 22)))
    print(Pokemon("Fire", 45).advantage(Pokemon("Water", 22)))
