Word Segmentation
Cecilia Zhou and Haoqing Wang

Run "python example.py" in the terminal to see the results for an example.

Customize your dictionary by modifying the file "twoletter.txt", which currently holds two-letter words allowed in scrabble but are generally not commonly used words. Add words (not necessarily length 2) to ignore in "twoletter.txt", and run "helpers.modifyDictionary()" if you want to remove them from your PyEnchant dictionary. The words removed and added in "modifyDictionary()" are what we use.


We also provide three other files, testSameText.py, testSimilarText.py, testCompareAlgs.py. 

The first runs the dynamic programming algorithm using transition frequencies on the same text as the base text, assuming that the user chooses to use the default base text. The second runs that algorithm on a similar text ``The Old Man and the Sea", written by Ernest Hemingway as is the default base text. The third compares the four different algorithms' run-times and accuracy for three different texts. The first text is the same as in example.py, the second is an excerpt from the song ``Sorry" by Justin Bieber, and the third is just a nonsensical sentence that illuminates some interesting behavior of our algorithms discussed earlier.


If one wants to run our algorithms on different texts, just run "python testYourOwnText.py" in the the terminal, and input the text file of your choice when prompted and then input the base text file of your choice when prompted as well. 
