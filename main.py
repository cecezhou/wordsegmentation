import models
import re
import enchant
import parsebasetext

# print freq_dict
# get frequencies of transitions 
# text = "thequickbrownfoxjumpsoverthelazydog"

text = "willIfinishthisproblemsetintimeforvanillawhataresomewordsthatmightnotworkoutchocolatedon't"
# text = "paidforsleepingtogetherThiswastheendofthetrapThiswaswhatpeoplegotforlovingeachotherThankGodforgasanywayWhatmustithavebeenlikebeforetherewereanaestheticsOnceitstartedtheywereinthemillraceCatherinehadagoodtimeinthetimeofpregnancyItwasn'tbadShewashardlyeversickShewasnotawfullyuncomfortableuntiltowardthelastSonowtheygotherintheend"
# text = open('condensed.txt').read()
# text = "I'mgoingtolifesciencesclass"
print text
mytext = models.NoSpaceText(text, 15)
print mytext.dpGreedy()
print mytext.getBestSeg()

#mytext.getFreq('alphanumeric.txt')
# print mytext.classicalSolve()

print "DP:"
# mytext.getFreq("alphanumeric.txt")
# mytext.getTransitionFreq("alphanumeric.txt")

print mytext.dpGreedy(transFreq = True)

print mytext.getBestSeg()

# mytext.spaces = [0,1,0,0,0,0]
# print mytext.printText()

# mytext.adjustVariable(1, 1)
# mytext.adjustVariable(5, 1)
# mytext.adjustVariable(7, 1)
# mytext.adjustVariable(13, 1)

# print mytext.checkFactor(0)
# print mytext.checkFactor(1)
# print mytext.checkFactor(2)
# print mytext.checkFactor(3)
# print mytext.checkFactor(4)
# print mytext.checkFactor(5)

# print mytext.getFactor(0)
# print mytext.getFactor(1)
# print mytext.getFactor(2)
# print mytext.getFactor(3)
# print mytext.getFactor(4)
# print mytext.getFactor(5)

# print mytext.getText()
# print mytext.classicalSearch()
