import models

text = "mynameissteddythisisalongsentencepleaseworkthankyou"

mytext = models.NoSpaceText(text, 10)
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

print mytext.dpSearch()
print mytext.getText()

assignment = [0] * 7
# print mytext.checkAssignment(assignment)

