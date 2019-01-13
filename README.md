# Data Model

## case class
ClassName = collection.namedtuple('ClassName', [attr1, attr2, ...])

## len()
The implementation of `__len__(self)` 
	
	len(ClassName)

## iteration and slicing
The implementation of `__getitem__(self)`
	
	deck[0], deck[:3], deck[1::2]  # slicing
	  
	for card in deck:  # iteration
		print(card)

## sorting
Define the key function to return the rank value. Note that the key in `dict()` cannot be string type(because it is intepreted as a symbol?).

	suit_values = dict(spades=1, diamonds=2, clubs=3, hearts=4)
	print(suit_values)
     
	def spade_high(card):
		rank_index = FrenchDeck.ranks.index(card.rank)
		print(rank_index)
		return rank_index * len(suit_values) + suit_values[card.suit]


