#player selects high card or blackjack

player_name = input('Enter your name  ')
starting_balance = input('Enter your starting balance  ')

class Card:
    def __init__(self, value, symbol, suit):
        self.value = value
        self.symbol = symbol
        self.suit = suit


deck_number = 0
card_set = []
suits = ['diamonds', 'hearts', 'clubs', 'spades']
symbols = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def populate_cards(self):
    global card_set
    for i in range (self):
        card_set += [Card(value, symbol, suit) for value in range(2, 15) for symbol in symbols for suit in suits]
        i += 1
    print(card_set)

def number_of_decks():
    global deck_number
    while type(deck_number) != 'int' or deck_number < 1:
        try:
            num_decks = int(input('How many decks do you want to use?  '))
            if num_decks > 0:
                deck_number = num_decks
                populate_cards(deck_number)
            else:
                print('please enter a positive integer')
                continue
        except ValueError:
            print('please enter a positive integer')
            continue
        else:
            break


number_of_decks()



class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance



you = Player(player_name, starting_balance)
print ('Welcome, ' + you.name + '.  Your starting balance is ' + you.balance + '.')

dealer = Player('Dealer', 0)

for i in card_set:
    print(i.symbol, i.suit)

bet = 0
#def bet():
    

#modify deck as game is played, shuffle when needed M

#for high card, select card for player and dearler M
    #announce higher card/suit as winner M
    #player doubles or loses their bet S

#for blackjack, deal 2 cards each: player -> dealer -> player -> dealer C
    #dealer's second card is not printed so player can't see it Cm
    #if player or dealer has blackjack, instantly end round Cm
        #ask for insurance if dealer has ace face up Cs
    #player hits or stays Cm
        #also can double down (or split when both cards have same value) Cs
        #doubles bet and deals one card for double down, or splits cards into two hands Cs
    #player busts if over 21 Cm
    #dealer hits until they have 17 or higher, busts if they exceed 21 Cm
        #dealer hits on soft 17 (ace 6) Cs
    #if neither busts, higher hand wins (push if both hands are equal)

#track wins and losses M
    #track net amount of money won/lost S

#write tests for anything that needs tested M
    #make sure to return statements for invalid inputs M