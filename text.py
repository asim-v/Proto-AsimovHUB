def findB():
	"How many counts can i fabricate with 36 number cards"
	count = 0
	bag = 350
	while bag > 0:
		print(count,bag)	
		count += 1
		bag -= len(str(count))

def genPlace(num):
	l = []
	for x in range(num):
		l.append('p')
		l.append('c')
		l.append('d')
		l.append('m')

	return l[num-1]

print(genPlace(402))