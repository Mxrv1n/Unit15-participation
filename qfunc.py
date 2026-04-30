import matplotlib.pyplot as plt
from random import randint

class card:
    def __init__(self):
        self.suit = randint(1,5)
        self.rank = randint(1,14)
    
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit

class dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides + 1)
# queen = 13 
def simulate_card_game():
    if True:
        points = 1
    card1 = card()
    d12 = dice(12)
    d4 = dice(4)
    d20 = dice(20)

    if card1.get_rank() == 13:
        if d20.roll() == 20:
            points = 20 * points

    elif card1.get_suit() == d12.roll():
        points += points
        if card1.get_rank() == d4.roll():
            points += 5*points
    
    return points
if __name__ == "__main__":
    list = []
    for i in range(10000000):
        list.append(simulate_card_game())

    plt.hist(list, bins=10)
    plt.xlabel("Points")
    plt.ylabel("Frequency")
    plt.title("Distribution of Points in Card Game")
    plt.show()
