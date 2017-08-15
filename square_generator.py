def lazy_integers(n=0):
	while True:
		yield n
		n += 1

xs = lazy_integers()

next(xs)

squares = (x**2 for x in lazy_integers())
doubles = (2*x for x in lazy_integers())