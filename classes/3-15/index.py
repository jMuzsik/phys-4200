import numpy as np
import random

# single player game
# basically, 8 cards and see if those cards become a 3 of a kind

def is_three_of_a_kind(cards):
  amount = {}
  for i in range(len(cards)):
    card = cards[i]
    num = card.split()[0]
    # this is currently not necessary
    # if available[card]:
    #   available[card] = False
    if num in amount:
      amount[num] += 1
    else:
      amount[num] = 1
  for _, val in amount.items():
    if val >= 3:
      return True
  return False

def run_sim(n):
  suits = ['\u2661', '\u2662', '\u2663', '\u2664']
  cards = []

  # create deck of cards in order
  for i in range(len(suits)):
    suit = suits[i]
    for j in range(13):
      cards.append(str(j) + " " + suit)

  res = 0
  for i in range(n):
    random.shuffle(cards)
    # available = np.full(1, 52, True, dtype=bool)
    # give out 8 cards (as all I care about is if 3 of a kind occurs)
    if is_three_of_a_kind(cards[:8]):
      res += 1

  return res

def sim_four_players(n):
  suits = ['\u2661', '\u2662', '\u2663', '\u2664']
  cards = []

  # create deck of cards in order
  for i in range(len(suits)):
    suit = suits[i]
    for j in range(13):
      cards.append(str(j) + " " + suit)

  res = 0
  for i in range(n):
    random.shuffle(cards)
    # available = np.full(1, 52, True, dtype=bool)
    # this is now turn by turn
    # 1. 4 players
    # 2. each round, who goes first is updated (start with you going first, then next player)
    # 3. each player is dealt 5 cards in order within shuffled deck
    # 4. other players get random amount of cards (0 - 3)
    # 6. count the amount of each num of cards that you have, discard ones that have
    #    low chance of being 3 of a kind
    #    - Go through 5 cards, see if there are 2 of a kind, if so, keep those cards,
    #      else randomly discard 1 of a kinds
    you = 1
    your_cards = []
    players = [1,2,3,4]
    while True:
      for i in range(len(players))
      break
    if is_three_of_a_kind(cards[:8]):
      res += 1

  return res

n = 100000
# print(float(run_sim(n)) / n)
