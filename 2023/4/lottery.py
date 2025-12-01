from dataclasses import dataclass

max_card_id = 204

@dataclass
class Card:
    id: int
    winning_numbers: list[int]
    numbers: list[int]

    def points(self):
        points = 0
        for number in self.numbers:
            if number in self.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        return points

    @property
    def matching_numbers(self):
        return [number for number in self.numbers if  number in self.winning_numbers]

    def copies(self):
        if self.matching_numbers:
            return [self.id + idx for idx in range(1,len(self.matching_numbers)+1)]
        return []

def clean(numbers):
    split_nums = numbers.strip().split(" ")
    print(split_nums)
    return [eval(num.strip()) for num in split_nums if num]

def recurse_copies(cards, current_id):
    count = len(cards[current_id].copies())
    for copy in cards[current_id].copies():
        if cards[copy].copies():
            count += recurse_copies(cards, copy)
    print(current_id, cards[current_id].copies(), count)
    return count

cards = {}  
card_id = 1
with open("input_4.txt") as f:
    for line in f:
        _,card_input = line.split(":")
        winning,scratched = card_input.strip().split("|")
        cards[card_id] = Card(card_id, clean(winning), clean(scratched))
        card_id += 1

print([card.matching_numbers for card in cards.values()])
# print(sum([card.points() for card in cards]))

total_cards = 0
for id,card in cards.items():
    total_cards += recurse_copies(cards, id)
    total_cards += 1

print(total_cards)