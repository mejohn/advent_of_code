from collections import Counter
mapping = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def count_hand(hand):
    cards = [mapping[char] for char in hand]
    counter = Counter(cards)
    jokers = counter.get(1, 0)
    if jokers:
        max_count = max(counter, key=lambda x: counter[x])
        if max_count == 1:
            if len(counter.values()) != 1:
                counter.pop(1)
                max_count = max(counter, key=lambda x: counter[x])
                counter[max_count] += jokers
        else:
            del counter[1]
            counter[max_count] += jokers
    if sum(counter.values()) != 5:
        print(counter, hand)
    hand_type = 0
    if len(counter.values()) == 1:
        hand_type = 7
    if len(counter.values()) == 5:
        hand_type = 1
    if len(counter.values()) == 2:
        if 4 in counter.values():
            hand_type = 6 # four of a kind
        else:
            # 3 2
            hand_type = 5 # full house
    if len(counter.values()) == 3:
        if Counter([2,1,2]) == Counter(counter.values()):
            hand_type = 3 # two pair
        else:
            # 3 1 1 
            hand_type = 4 # 3 of a kind
    if len(counter.values()) == 4:
            hand_type = 2
    return hand_type, tuple(cards)

hands = []
with open("input_7.txt") as f:
    for line in f:
        hand,bid = line.strip().split(" ")
        hand_type,points = count_hand(hand)
        hands.append((hand_type, points, int(bid.strip())))

ranked_hands = sorted(hands, key=lambda x: (x[0], x[1]))

total_points = []
for idx,hand in enumerate(ranked_hands):
    # print(idx+1, hand, (idx+1)*hand[2])
    total_points.append((idx+1)*hand[2])

print(sum(total_points))