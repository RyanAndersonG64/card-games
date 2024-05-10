import random

high_card = True
game = input('Welcome to high card.  If you would like to play blackjack, enter "blackjack".  Enter anything else to continue to high card.  ')
if game == 'blackjack':
    high_card = False
    print('Initializing blackjack')
else:
    print('Initializing high card')

        
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Player:
    name = input('Enter your name  ')
    def init_balance(self):
        starting_balance = 0
        while type(starting_balance) != 'int' or starting_balance < 1:
            try:
                sb = int(input('Enter your starting balance  '))
                if sb > 0:
                    return sb
                else:
                    print ('please enter a positive integer')
                    continue
            except ValueError:
                print('please enter a positive integer')
                continue
            else:
                break
    def __init__(self):
        self.name = self.name
        self.balance = self.init_balance()
        self.hand = None
        self.wins = 0
        self.bet = 0
        print ('Welcome, ' + self.name + '.  Your starting balance is ' + str(self.balance) + '.')



suits = {'clubs' : 0.1, 'diamonds' : 0.2, 'hearts' : 0.3, 'spades' : 0.4}

if high_card == True:
    values = {'2' : 2, '3': 3, '4': 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K': 13, 'A' : 14}
else:
    values = {'2' : 2, '3': 3, '4': 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K': 10, 'A' : 11}

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in values for suit in suits]
        self.decks = self.number_of_decks()
    def __len__(self):
        return len(self.cards)
    def number_of_decks(self):
        deck_number = None
        while type(deck_number) != 'int' or deck_number < 1:
            try:
                num_decks = int(input('How many decks do you want to use?  '))
                if num_decks > 0:
                    deck_number = num_decks
                    for i in range(1, deck_number):
                        self.cards.append([Card(value, suit) for value in values for suit in suits])
                else:
                    print('please enter a positive integer')
                    continue
            except ValueError:
                print('please enter a positive integer')
                continue
            else:
                break



class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = None
        self.wins = 0






you = Player()
dealer = Dealer()

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

class Game:
    def __init__(self):
        temp_deck = Deck()
        random.shuffle(temp_deck.cards)
        self.deck = temp_deck
        
    def create_new_deck(self):
        temp_deck = Deck()
        random.shuffle(temp_deck.cards)
        self.deck = temp_deck


game = Game()

class PlayHighCard:    
    def deal(self):
        you.hand = game.deck.cards[0]
        print(f'Your card is a {you.hand.value} of {you.hand.suit}')
        game.deck.cards.remove(you.hand)
        dealer.hand = game.deck.cards[0]
        print(f"Dealer's card is a {dealer.hand.value} of {dealer.hand.suit}")
        game.deck.cards.remove(dealer.hand)

    def win_check(self):
        your_value = you.hand.value + you.hand.suit
        dealers_value = dealer.hand.value + dealer.hand.suit
        if your_value > dealers_value:
            you.balance += bet
            print('You win!  Your balance is now ' + str(you.balance))
            you.wins += 1
            print(f'You have won {you.wins} hands and lost {dealer.wins} hands this session, with {self.draws} draws')
        elif dealers_value > your_value:
            you.balance -= bet
            print('You lose!  Your balance is now ' + str(you.balance))
            dealer.wins += 1
            print(f'You have won {you.wins} hands and lost {dealer.wins} hands this session, with {self.draws} draws')
        else:
            print('Draw!  Your balance is still ' + str(you.balance))
            self.draws += 1
            print(f'You have won {you.wins} hands and lost {dealer.wins} hands this session, with {self.draws} draws')
        if len(game.deck.cards) == 0:
            game.create_new_deck()
        if you.balance < 1:
            print('You have run out of money.  Game over.')
        else: pass
        play_again = input('Enter "y" if you would like to play again.  Any other input will end the game.  ')
        if play_again == 'y' and you.balance > 0:
            PlayHighCard()

    def __init__(self):
        self.draws = 0
        self.bet = place_bet()
        self.hands = self.deal()
        self.end_round = self.win_check()

if high_card == True:
    PlayHighCard()







# def play_blackjack():
#     global deck
#     global your_wins
#     global dealer_wins
#     global draws
#     global insurance
#     insurance = ''
#     end_turn = False
#     global next_card_selector
#     global next_card
#     place_bet()
#     your_first_card_selector = random.randint(0, len(deck.cards) - 1)
#     your_first_card = deck.cards[your_first_card_selector]
#     deck.cards.remove(your_first_card)
#     dealers_first_card_selector = random.randint(0, len(deck.cards) - 1)
#     dealers_first_card = deck.cards[dealers_first_card_selector]
#     deck.cards.remove(dealers_first_card)
#     your_second_card_selector = random.randint(0, len(deck.cards) - 1)
#     your_second_card = deck.cards[your_second_card_selector]
#     deck.cards.remove(your_second_card)
#     dealers_second_card_selector = random.randint(0, len(deck.cards) - 1)
#     dealers_second_card = deck.cards[dealers_second_card_selector]
#     deck.cards.remove(dealers_second_card)
#     #aces are 1 or 11 Cm
#     your_total = your_first_card.value + your_second_card.value
#     dealer_total = dealers_first_card.value + dealers_second_card.value
#     print(f'Your hand is {your_first_card.value, your_first_card.suit} and {your_second_card.value, your_second_card.suit}')
#     print(f"Dealer's face up card is {dealers_first_card.value, dealers_first_card.suit}")
#     if dealers_first_card.value == 'A':
#         insurance = input('Dealer has an ace.  Enter "yes" if you would like insurance, or anything else if you do not want insurance  ')
#     if your_first_card.value + your_second_card.value == 21 and dealers_first_card.value + dealers_second_card.value != 21:
#         you.balance += bet * 1.5
#         print('You have blackjack! You win 1.5x your bet.  Your balance is now ' + str(you.balance))
#     elif your_first_card.value + your_second_card.value != 21 and dealers_first_card.value + dealers_second_card.value == 21:
#         you.balance -= bet
#         #add condition for insurance
#         print('Dealer has blackjack. You lose.  Your balance is now ' + str(you.balance))
#     elif your_first_card.value + your_second_card.value == 21 and dealers_first_card.value + dealers_second_card.value == 21:
#         #add condition for insurance
#         print('You and the dealer both have blackjack.  You push.  Your balance is still ' + str(you.balance))
#     else:
#         while end_turn == False:
#             action = input('You haveWhat would you like to do?  Enter "hit" to hit, "double" to double down, "split" to split, or anything else to stand  ')
#             if action == 'split' and your_first_card.value != your_second_card.value:
#                 print('You can only split if your cards have the same value')
#                 continue
#             #elif action == 'split' and your_first_card.value == your_second_card.value:
#                 #split cards into two hands, each eith their own bet
#             elif action == 'hit':
#                 next_card_selector = random.randint(0, len(deck.cards) - 1)
#                 next_card = deck.cards[your_first_card_selector]
#                 deck.cards.remove(next_card)
#                 continue
#             elif action == 'double down':
#                 bet = bet * 2
#                 #add one card
#                 end_turn = True
#             else:
#                 end_turn = True

    #player hits or stays Cm
        #also can double down (or split when both cards have same value) Cs
        #doubles bet and deals one card for double down, or splits cards into two hands Cs
    #player busts if over 21 Cm
    #dealer hits until they have 17 or higher, busts if they exceed 21 Cm
        #dealer hits on soft 17 (ace 6) Cs
    #if neither busts, higher hand wins (push if both hands are equal)


    #track net amount of money won/lost S

#write tests for anything that needs tested M
    #make sure to return statements for invalid inputs M

from unittest.mock import Mock, patch

Mock().Player.init_balance()

def test_init_balance_pos_int():
    with patch('builtins.input', new=Mock(return_value='1')):
        assert Player.init_balance() == 1

def test_init_balance_neg_int():
     with patch('builtins.input', new=Mock(return_value='-1')):
         assert Player.init_balance() == 'please enter a positive integer'

def test_init_balance_str():
    with patch('builtins.input', new=Mock(return_value='this is not a balance')):
        assert Player.init_balance() == 'please enter a positive integer'
        
#tests:

    #input balance
    #input number of decks
    #place bet
    #game is played
    #play again?