import models
import re


# replace hyphen \n's and all double quotes
string = open('farewell_to_arms.txt').read()
new_str = re.sub('[^a-zA-Z\n\']', ' ', string)
new_str.replace(' \' ','')
open('alphanumeric.txt', 'w').write(new_str)

text = "mynameisteddyhiwhat"

mytext = models.NoSpaceText(text, 10)


# get frequencies of transitions

# 



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

# assignment = [0, None, None, None, None, None, ]

# print mytext.classicalSolve()
# print mytext.getText()

# assume words given sentence length is Normal
# use chars per word distribution
