import random

high_card = True
game = input('Welcome to high card.  If you would like to play blackjack, enter "blackjack".  Enter anything else to continue to high card.  ')
if game == 'blackjack':
    high_card = False

player_name = input('Enter your name  ')
starting_balance = 0
def init_balance():
    global starting_balance
    while type(starting_balance) != 'int' or starting_balance < 1:
        try:
            sb = int(input('Enter your starting balance  '))
            if sb > 0:
                starting_balance = sb
            else:
                print('please enter a positive integer')
                continue
        except ValueError:
            print('please enter a positive integer')
            continue
        else:
            break
init_balance()

        
class Card:
    def __init__(self, value, suit):
        # self.symbol = symbol
        self.value = value
        self.suit = suit


suits = {'clubs' : 0, 'diamonds' : 1, 'hearts' : 2, 'spades' : 3}
values = {'2' : 2, '3': 3, '4': 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K': 13, 'A' : 14}
#add separate blackjack values

deck_number = 0
def number_of_decks():
    global deck_number
    global decks
    while type(deck_number) != 'int' or deck_number < 1:
        try:
            num_decks = int(input('How many decks do you want to use?  '))
            if num_decks > 0:
                deck_number = num_decks
            else:
                print('please enter a positive integer')
                continue
        except ValueError:
            print('please enter a positive integer')
            continue
        else:
            break


number_of_decks()
class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in values for suit in suits]
        for i in range(1, deck_number):
            self.cards.append([Card(value, suit) for value in values for suit in suits])
    def __len__(self):
        return len(self.cards)

deck = Deck()

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance



you = Player(player_name, starting_balance)
print ('Welcome, ' + you.name + '.  Your starting balance is ' + str(you.balance) + '.')

dealer = Player('Dealer', 0)

bet = 0
def place_bet():
    global bet
    while type(bet) != 'int':
        try:
            next_bet = int(input('Place your bet:  '))
            if next_bet <= you.balance and next_bet > 0:
                bet = next_bet
                break
            else:
                print('You cannot bet more than your current balance or less than 1')
                continue
        except ValueError:
            print('please enter a positive integer')
            continue
        except TypeError:
            print('please enter a positive integer')
            continue

random.shuffle(deck.cards)
    
your_wins = 0
dealer_wins = 0
draws = 0
def play_high_card():
    global deck
    global your_wins
    global dealer_wins
    global draws
    place_bet()
    your_card_selector = random.randint(0, len(deck.cards) - 1)
    your_card = deck.cards[your_card_selector]
    print(f'Your card is {your_card.value, your_card.suit}')
    deck.cards.remove(your_card)
    dealers_card_selector = random.randint(0, len(deck.cards) - 1)
    dealers_card = deck.cards[dealers_card_selector]
    print(f"Dealer's card is {dealers_card.value, dealers_card.suit}")
    deck.cards.remove(dealers_card)
    if your_card.value > dealers_card.value:
        you.balance += bet
        print('You win!  Your balance is now ' + str(you.balance))
        your_wins += 1
        print(f'You have won {your_wins} hands and lost {dealer_wins} hands this session, with {draws} draws')
    elif dealers_card.value > your_card.value:
        you.balance -= bet
        print('You lose!  Your balance is now ' + str(you.balance))
        dealer_wins += 1
        print(f'You have won {your_wins} hands and lost {dealer_wins} hands this session, with {draws} draws')
    elif your_card.value == dealers_card.value and your_card.suit > dealers_card.suit:
        you.balance += bet
        print('You win!  Your balance is now ' + str(you.balance))
        your_wins += 1
        print(f'You have won {your_wins} hands and lost {dealer_wins} hands this session, with {draws} draws')
    elif your_card.value == dealers_card.value and dealers_card.suit > your_card.suit:
        you.balance -= bet
        print('You lose!  Your balance is now ' + str(you.balance))
        dealer_wins += 1
        print(f'You have won {your_wins} hands and lost {dealer_wins} hands this session, with {draws} draws')
    else:
        print('Draw!  Your balance is still ' + str(you.balance))
        draws += 1
        print(f'You have won {your_wins} hands and lost {dealer_wins} hands this session, with {draws} draws')

    if you.balance < 1:
        print('You have run out of money.  Game over.')
    print(len(deck.cards))
    if len(deck.cards) < 26 * deck_number:
       deck = Deck()
       random.shuffle(deck.cards)
    play_again = input('Enter "y" if you would like to play again.  Any other input will end the game.  ')
    if play_again == 'y' and you.balance > 0:
        play_high_card()
    else: pass

if high_card == True:
    play_high_card()




#for blackjack, deal 2 cards each: player -> dealer -> player -> dealer C
    #aces are 1 or 11 Cm
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