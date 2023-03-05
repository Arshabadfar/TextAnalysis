class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
               
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        # The split function returns a list!
        wordList = self.fmtText.split(' ')
        # Create dictionary
        # Here is how to add data to a Dictionary
        self.freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            self.freqMap[word] = wordList.count(word)
      
        return self.freqMap
      
    def freqWord(self,word):
        if word in self.freqMap:
            return self.freqMap[word]
        else:
            return 0


samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
print(samplePassage.freqAll())
samplePassage.freqWord("et")     
