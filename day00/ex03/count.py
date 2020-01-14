import sys
import string

def text_analyzer(txt=''):
	"""	This function counts the number of upper characters, 
	lower characters, punctuation and spaces in a given text."""
	if len(txt) == 0:
		txt = input("What is the text to analyse ?")
	strlen = len(txt)
	out = "The text contains {} characters:"
	print(out.format(strlen))
	#-----------------------#
	up = 0
	for x in txt:
		if x in string.ascii_uppercase:
			up += 1
	upper = "- {} upper letters"
	print(upper.format(up))
	#-----------------------#
	low = 0
	for x in txt:
		if x in string.ascii_lowercase:
			low += 1
	lower = "- {} lower letters"
	print(lower.format(low))
	#-----------------------#
	pt = 0
	for x in txt:
		if x in string.punctuation:
			pt += 1
	pts = "- {} punctuation marks"
	print(pts.format(pt))
	#-----------------------#
	s = txt.count(' ')
	space = "- {} spaces"
	print(space.format(s))