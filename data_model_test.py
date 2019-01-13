from data_model import FrenchDeck 

deck = FrenchDeck()
print(len(deck))


print(deck[0], deck[-1])

from random import choice

print(choice(deck))

for i, card in enumerate(deck):
	if i <= 4:
		print(card)


suit_values = dict(spades=1, diamonds=2, clubs=3, hearts=4)
print(suit_values)

def spade_high(card):
	rank_index = FrenchDeck.ranks.index(card.rank)
	print(rank_index)
	return rank_index * len(suit_values) + suit_values[card.suit]



for i, card in enumerate(sorted(deck, key=spade_high)):
	if i <= 4:
		print(card)

print(FrenchDeck.ranks)