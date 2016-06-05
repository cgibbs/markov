import json
import pickle
import random
import re

def getRand(dct):
	return random.choice(dct.keys())

# markov = pickle.load(open("markov2.p", "rb"))	
# markovStarts = pickle.load(open("starts2.p", "rb"))

markovStarts = []
markov = {}

with open("starts.json", "rb") as f:
	markovStarts = json.loads(f.read())

with open("markov.json", "rb") as f:
	markov = json.loads(f.read())

i = 0
bail = False
with open("markovOut2.txt", "wb") as f:
	while i < 100:
		start = random.choice(markovStarts)
		if(start in markov):
			next = random.choice(markov[start])
		else:
			continue
		s = ' '.join(start.split('.')) + " " + next
		k = start.split('.')[1] + '.' + start.split('.')[2] + '.' + next
		while (len(next) > 0 and next[-1] != '.' and next[-1] != '?'):
			temp = k.split('.')[1] + '.' + k.split('.')[2]
			if(k in markov):
				next = random.choice(markov[k])
			else:
				s = ""
				break
			s += " " + (next or '.')
			k = temp + '.' + next
		if s:
			f.write(s + "\n")
			i += 1