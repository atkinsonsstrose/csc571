import sys
countrySales = {}
for line in sys.stdin:
	line = line.strip()
	country, total = line.split('\t', 1)
	try:
		total = float(total)
	except ValueError: pass
	try:
		countrySales[country] = countrySales[country] + total
	except:
		countrySales[country] = total
for country in countrySales.keys():
    print '%s\t%s'% (country, countrySales[country])