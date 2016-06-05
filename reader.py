import json
import pickle
import re

markov = {}	
markovStarts = []
with open("corpus.txt", "r") as corpus:
	for line in corpus.readlines():
		splitLine = re.findall(r"[\w]+\'*[\.\?\,]*", line)
		if len(splitLine) > 2:
			markovStarts.append(splitLine[0] + '.' + splitLine[1] + '.' + splitLine[2])
			for i in range(len(splitLine[:-1]) - 2):
				#if splitLine[i] and splitLine[i+1] and splitLine[i+2]:
				if (splitLine[i] + '.' + splitLine[i+1] + '.' + splitLine[i+2] in markov):
					markov[splitLine[i] + '.' + splitLine[i+1] + '.' + splitLine[i+2]].append(splitLine[i+3])
				else:
					markov[splitLine[i] + '.' + splitLine[i+1] + '.' + splitLine[i+2]] = [splitLine[i+3]]

with open("starts.json", "wb") as f:
	f.write(json.dumps(markovStarts))

with open("markov.json", "wb") as f:
	f.write(json.dumps(markov))