import models
import re
import enchant
import parsebasetext


text = open('condensed.txt').read()
print text

mytext = models.NoSpaceText(text, 15)

print "DP: naive probability"


mytext.dpGreedy()
print mytext.getBestSeg()

print "DP: transition probability"


mytext.dpGreedy(transFreq = True)

print mytext.getBestSeg()

