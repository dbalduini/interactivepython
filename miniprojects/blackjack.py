# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class        
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = 'Hand Contains '
        for c in self.cards:
            s = s + str(c) + ' '
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = aces = 0
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A':
                aces += 1
            value += VALUES[rank]
        if aces >= 1:
            if (value + 10) <= 21:
                value += 10
        return value
   
    def draw(self, canvas, pos):
        space = CARD_SIZE[0]
        for card in self.cards:
            card.draw(canvas, [space, pos])
            space += CARD_SIZE[0] + 10


# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return random.choice(self.cards)
    
    def __str__(self):
        s = 'Deck Contains '
        for c in self.cards:
            s = s + str(c) + ' '
        return s



#define event handlers for buttons
def deal():
    global outcome, in_play, score, message
    global deck, player, dealer
    
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    print 'Player', player
    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    print 'Dealer', dealer
    
    outcome = "Hit or stand?"
    message = ""
    
    if in_play:
        print 'Player lost'
        score -= 1
    else:
        in_play = True

def hit():
    global in_play, player, deck, outcome, score, message
    if in_play:     
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
        
        if player.get_value() > 21:
            message = 'You went bust and lose!'
            outcome = 'New deal?'
            score -= 1
            in_play = False
       
def stand():
    global score, in_play, message, outcome    
    global dealer, deck
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() <= 17:
            dealer.add_card(deck.deal_card())

        if dealer.get_value() > 21:
            message = 'Dealer went busted. You Win!'
            score += 1
        else:
            if player.get_value() <= dealer.get_value():
                message = 'You Lose!'
                score -= 1
            else:
                message = 'You Win!'
                score += 1

    outcome = 'New deal?'                
    in_play = False

# draw handler    
def draw(canvas):
    global player, dealer
    dealer.draw(canvas, 200)
    player.draw(canvas, 400)
    
    margin_left = CARD_SIZE[0]
    margin_right = 330
    
    # Hide the first card of the dealer
    if in_play:
        center_dest = [margin_left + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]]
        canvas.draw_image(card_back, 
                          CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          center_dest, CARD_BACK_SIZE)        
    
    canvas.draw_text('Blackjack', [50, 70], 34, 'Cyan')    
    canvas.draw_text('Score ' + str(score), [margin_right, 70], 27, 'White')
    canvas.draw_text('Dealer', [margin_left, 180], 20, 'Black')
    canvas.draw_text(message, [margin_right, 180], 20, 'White')    
    canvas.draw_text('Player', [margin_left, 380], 20, 'Black')
    canvas.draw_text(outcome, [margin_right, 380], 20, 'White')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric