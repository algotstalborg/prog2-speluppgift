class Player:
    def __init__(self, hp_mult, energy_add, gold_mult, handsize_add):
        self.maxhp = 100 * hp_mult
        self.hp = self.maxhp
        self.energy = 3 + energy_add
        self.gold = 100 * gold_mult
        self.handsize = 2 + handsize_add
        self.deck = []
        self.target = object

class Enemy:
    def __init__(self):
        pass

class Card:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value

class Slash(Card):
    def __init__(self, name, cost, value):
        super().__init__(name, cost, value)
    def play_card(self):
        pass

warrior_start_deck = []
barbarian_start_deck = []
mechant_start_deck = []
available_cards = []
available_rare_cards = []
deck = []

while True:
    # Character creation

    print('''
Welcome!
Would you kindly state your proffesion?
1. Warrior
2. Barbarian
3. Merchant
    ''')
    while True:
        class_choice = input()
        if class_choice == 1 or class_choice.lower == 'warrior':
            player = Player(1, 0, 1, 0)
        elif class_choice == 2 or class_choice.lower == 'barbarian':
            player = Player(0.7, 1, 1, 0)
        elif class_choice == 3 or class_choice.lower == 'merchant':
            player = Player(0.9, 0, 2, 1)
        else:
            print("something went wrong!")
            continue
        break

    print('''
    The whale says hi
    1. + 50 gold
    2. + 1 card
    3. + 1 rare card - 20 max hp
    ''')
    while True:
        whale_choice = input()
        if whale_choice == 1 or whale_choice.lower == 'gold':
            player.gold += 50
        elif whale_choice == 2 or whale_choice.lower == 'card':
            player
        elif whale_choice == 3 or whale_choice.lower == 'rare card':
            player.maxhp -= 20
        else:
            print("something went wrong!")
            continue
        break        

    