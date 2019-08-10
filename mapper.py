import sys
for line in sys.stdin:
	line = line.strip()
	tokens = line.split(',')
	try:
		country = tokens[7]
		price = float(tokens[5])
		qty = int(tokens[3])
		print '%s\t%s' % (country, (price*qty))
	except ValueError: pass