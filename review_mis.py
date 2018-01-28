#!/usr/bin/env python
import random
import os

with open('./mistake.txt','r') as f:
    data = f.readlines()

count = raw_input("How many words do you want to review on your mistake ?\n")

for x in xrange(int(count)):
    for line in data:
        words = line.split(";")
        ask = random.sample(words,1)
        print "Please answer 'y' or 'n' to the vocalbularies:"
        ans = raw_input(ask)
        if ans == "n":
            with open('./mistake.txt','a') as m:
                question = str(ask)
                m.write(question.strip("['']") + ";")
        elif ans == "y":
            pass
        else:
            print "I tell you already, make sure this is still your mistake\n"
            pass
