#! /usr/bin/env python
import sys
for line in sys.stdin:
    # split the line into words
    fields = line.strip().split("\t")
    text = fields[1]
    bigrams = [b for b in zip(text.split(" ")[:-1], text.split(" ")[1:])]
    for words in bigrams:
        print >> sys.stdout,'%s\t%s' % (words[0]+"-"+words[1],"1")
