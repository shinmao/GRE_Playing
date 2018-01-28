#!/usr/bin/env python
import random

print "                 _ooOoo_  "  
print "                o8888888o  " 
print "                88\" . \"88    "
print "                (| -_- |)    "
print "             ____/`---'\\____   "
print "           .'  \\|     |//  `.    "
print "           /  \\|||  :  |||//  \\    "
print "          /  _||||| -:- |||||-  \\    "
print "          |   | \\\\  -  /// |   |                 88888888888    8888888888   88888888888"
print "         | \\_|  ''\\---/''  |   |                 88       88    88      88   88"
print "          \\  .-\\__  `-`  ___/-. /                88             88      88   88"
print "         ___`. .'  /--.--\\  `. . __              88             888888888    8888888888"
print "      .\"\" '<  `.___\\_<|>_/___.'  >'\"\".           888888888888   8888         88"
print "     | | :  `- \\`.;`\\ _ /`;.`/ - ` : | |         88      8888   88  88       88"
print "   \\  \\ `-.   \\_ __\\ /__ _/   .-` /  /           88    88  88   88    88     88"
print "  =====`-.____`-.___\\_____/___.-`____.-'======   888888    88   88      88   88888888888"
print " `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      "
print " ~~~~~~~ A simple vocalbularies tool ~~~~~~~~~~     "
print " ~~~~~~~ 1. Learn new words with GRE.py ~~~~~~~     "
print " ~~~~~~~ 2. Review your mistake ~~~~~~~~~~~~~~~     "
print " ~~~~~~~ My code is ugly I know ~~~~~~~~~~~~~~~     "
print " ~~~~~~~ But I just want to memorize words!! ~~     "


with open('./dict.txt','r') as f:
    data = f.readlines()

count = raw_input("How many words do you want to learn ?\n")

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
            print "You dumb! I will add this vocalbulary to your mistake!\n"
