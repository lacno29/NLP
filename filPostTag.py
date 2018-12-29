import numpy
##Map POS
def englishTagger(lexicon):
    with open('POSTAG.txt') as fp:
        line = fp.readlines()
        cnt = 1
        x = 0
        tempList = []
        someBool = False
        for set in line:
            tags = set.split( )
            if lexicon.lower() == tags[1]:
                tempList = [lexicon,tags[0]]
                someBool = True
        if someBool is False:
            tempList = [lexicon, "N"]
            undDef(lexicon)
        return(tempList)
def undDef(lex):
    try:
        Und = open('list_of_new_undwords.txt',"a")
        Und.write("UND " +lex+"\n")
        Und.close()
    except FileNotFoundError:
        print("fnf")
##Create list for each mapped POS depending on input text
def createList(inputText):
    mappedList = []
    for someObj in inputText:
        tempList = englishTagger(someObj)
        mappedList.append(tempList)
    return(mappedList)
#def cvsWrite(cWrite):
    #csv = open("ouput.csv","w")
    #csv.split()
    #csv.write(cWrite)
def wInput():
    try:
        words = open('Postagged_words.txt',"w")
        reading = open('tokenized_words.txt',"r")
        check = reading.readlines()
        reading.close()
        for string in check:
            word_check = string.split()
            yeet = createList(word_check)
            #print(yeet)
            for each in yeet:
                bagong_var = each[0] +" "+ each[1]
                print(str(bagong_var))
                words.write(str(bagong_var+"\n"))
            #words.write(yeet)
            #return(yeet)
            #cvsWrite(yeet)
    except FileNotFoundError:
        print("fnf")
##MAIN
#open('tokenized_words.txt',"r")
#word = "ang baso ay laglag"
#list = []
#list = word.split(" ")
#print(word)
#print(list)
#mappedList = createList(list)
#print(mappedList)
wInput()
