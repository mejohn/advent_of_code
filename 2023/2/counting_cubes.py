from dataclasses import dataclass

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

@dataclass
class Game:
    red: int = 0
    blue: int = 0
    green: int = 0

    def assign(self, color, num):
        match color:
            case "red":
                self.red = num
            case "blue": 
                self.blue = num
            case "green":
                self.green = num

    @property
    def is_impossible(self):
        return self.red > MAX_RED or self.blue > MAX_BLUE or self.green > MAX_GREEN


@dataclass
class GameSet:
    id: int
    games: list[Game]
    min_red: int = 0
    min_blue: int = 0
    min_green: int = 0

    def any_impossible(self):
        return any([game.is_impossible for game in self.games])
    
    @property
    def power(self):
        return self.min_red * self.min_blue * self.min_green
    
    def set_mins(self):
        self.min_red = max([game.red for game in self.games])
        self.min_blue = max([game.blue for game in self.games])
        self.min_green = max([game.green for game in self.games])
    


game_sets = []
game_id = 1
with open("input_2.txt", "r") as f:
    for line in f:
        _, cubes = line.split(":")
        sets = cubes.strip().split(";")
        print(sets)
        games = []
        for set in sets:
            game = Game()
            for color_num in set.split(","):
                num,color = color_num.strip().split(" ")
                game.assign(color, eval(num))
            games.append(game)
        game_sets.append(GameSet(id=game_id, games=games))
        game_id += 1

print(game_sets)
passing_ids = []
for set in game_sets:
    if not set.any_impossible():
        passing_ids.append(set.id)

print(passing_ids)
print(sum(passing_ids))

powers = []
for set in game_sets:
    set.set_mins()
    powers.append(set.power)

print(powers)
print(sum(powers))