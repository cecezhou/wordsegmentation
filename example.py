import time
import re
import helpers
import models

shorttext= "thequickbrownfoxjumpsoverthelazydog"
print "Text: " + shorttext

mytext = models.NoSpaceText(shorttext, 15)

# process basetexts 
helpers.parseBaseText()

# get frequencies from base text
(freq_dict, normFactor) = helpers.getFreq("alphanumeric.txt")
(transition_freq_dict, transNormFactor) = helpers.getTransitionFreq("alphanumeric.txt")	

mytext.freq_dict = freq_dict
mytext.normFactor = normFactor
mytext.transition_freq_dict = transition_freq_dict
mytext.transNormFactor = transNormFactor

print "Segmenting Text..."

print "Classical Search: "

print mytext.classicalSearch()
print "Best Segmentation"
print mytext.getBestSeg()

print "\nDynamic Programming Approach: "

print mytext.dpSearch()
print mytext.getBestSeg()

print "\nDynamic Programming with Naive Frequency Approach"

print mytext.dpGreedy()
print mytext.getBestSeg()

print "\nDynamic Programming with Transition Frequency Approach"

print mytext.dpGreedy(transFreq = True)
print mytext.getBestSeg()

# text that should cause our algorithms to return None
badtext = "thequickbrownfoxjumpsovertheazydog"
print "\nText that shouldn't work: " + badtext

mytext = models.NoSpaceText(badtext, 15)

# store frequencies for new instance of NoSpaceText
mytext.transition_freq_dict = transition_freq_dict
mytext.transNormFactor = transNormFactor

print "\nResult: " + str(mytext.dpGreedy(transFreq = True)) + "\n"


