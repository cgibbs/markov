INTRO:
This is a quick and dirty Markov chain generator. reader.py reads the text you
give it, generates the Markov structure, and outputs it to a JSON string, so
that reading only has to take place once. markov.py reads from the generated
JSON files, and outputs 100 sentences.

Running over ~8.4MB of public domain Western novels takes about 4.8 seconds to
read and create the JSON files, and 2.3 seconds to load the JSON files and
generate 100 sentences. If you're thinking that cutting out the file IO would
make for a better single run, well, you're right. I wrote this for the type of
person who will generate sentences dozens of times to annoy their friends and
family, and it seemed more efficient to do the Markov structure generation
once.

If you're looking for pretty code so that you can give me a job offer, I
recommend my CGoL repo. It's way more interesting code than this hot mess.

HOW TO USE:
1. Drop all of the text you want to feed into the generator into a file named corpus.txt.
2. Run reader.py.
3. Run markov.py.
4. Read sentences from markovOut.txt.
