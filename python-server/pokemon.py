from poketype import poketypes

advantage_types = {1: "Advantage", 0: "Draw", -1: "Disadvantage"}


class Pokemon:
    def __init__(self, type, level):
        if type not in list(poketypes.keys()):
            raise ValueError("Unknown type of pokemon: " + str(type))
        try:
            if not isinstance(int(level), int):
                raise ValueError("Level of pokemon is not a number: " + str(level))
        except Exception:
            raise ValueError("Level of pokemon is not a number: " + str(level))
        if int(level) < 0:
            raise ValueError("Level of pokemon cannot be less than 0")
        self.type = type
        self.level = int(level)

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

    def check_odds(self, other):
        def advantage_value(p1, p2):
            if p1 > p2:
                return 1
            else:
                if p2 > p1:
                    return -1
                else:
                    return 0

        return advantage_types[advantage_value(self, other)]


if __name__ == '__main__':
    print(Pokemon("Fire", 23).check_odds(Pokemon("Water", 22)))
    print(Pokemon("Fire", 44).check_odds(Pokemon("Water", 22)))
    print(Pokemon("Fire", 45).check_odds(Pokemon("Water", 22)))
