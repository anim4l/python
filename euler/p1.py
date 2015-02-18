def getMultiples(n, limit):
	multiples = list()
	for i in range(1,limit):
		if (i%n == 0):
			multiples.append(i)
	return multiples

def add(x,y): return x+y

def p1(targets, limit):
	all = list()
	for t in targets:
		all = all + getMultiples(t,limit)
	all = list(set(all))
	print all
	return reduce(add,all)

finalSum = p1([3,5],1000)

print str(finalSum)