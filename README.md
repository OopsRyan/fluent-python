# Data Model

## case class
ClassName = collection.namedtuple('ClassName', [attr1, attr2, ...])

## len()
The implementation of `__len__(self)` 

**Note that len() for built-in types is super fast. Because there is no method call, it will read the value from the CPython's field.**

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

# Special methods (speical due to they are invoked by Python interpret.)
## __repr__
String representation, like toString in Scala

## __bool__
If `__bool__` is not implemented, `len()` will be invoked for an object. If its result is 0, then `bool(0)` will return `False`. `True` otherwise.

## __add__ , __mul__ , __abs__ ...

# List comprehension and generator expressions
Line breaks are ignored inside pairs of `[], {} or ()`, so you can build multi-line listcomps and genexps without using the ugly `\` line continuation escape.

These expressions have their own local scope like functions.

|   | Pros | Cons|
--- | --- | ---
| listcomp | objects are stored for late use | create each object in memory |
| genexps | yield items one by one using the iterator protocol. Especially for huge cartesian product | items are not stored |