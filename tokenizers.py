import re
import numpy as np
def sentenceNormalizer():

    nsfile = open('normalized_sentence.txt', 'w')

    try:        
        
        with open('inputParagraph.txt', 'r') as f:    
            for line in f:
                originalSentence = re.sub("\n", " ", line)
                print(originalSentence)
                #print("\n")
                
                with open('normalized_sentence.txt', 'a') as wf:
                    for sentences in originalSentence:
                        print(sentences)
                        wf.write(sentences)
                                         
    except:
        print("MANAMAJEFF")

def sentenceTokenizer():

    try:

        with open('normalized_sentence.txt', 'r') as f:    
            for line in f:
                sampleSentence = re.split(r'(?<!\w\.\w.)(?<![A-Z]\.)(?<![B][b]\.)(?<![G][n][g]\.)(?<![P][a][n][g]\.)(?<![G][a][t]\.)(?<![h][a][l]\.)(?<![G]\.)(?<![a][t][b][p])(?<=\.|\?)\s', line)
                print(sampleSentence)
                #print("\n")

                with open('splitted_sentence.txt', 'w') as wf:    
                    for sentences in sampleSentence:
                       ## print(sentences)
                        wf.write(sentences)
                        wf.write("\n")
                                         
    except:
        print("MANAMAJEFF")

def wordTokenizer():
    
    twfile = open('tokenized_words.txt', 'w')
    print("")

    try:

        with open('splitted_sentence.txt', 'r') as f:

            for line in f:
                sampleText = re.findall(r"[\w']+|[.,!?;-](?<![A-Z]\.)(?<![B][b]\.)(?<![G][n][g]\.)(?<![P][a][n][g]\.)(?<![G][a][t]\.)(?<![h][a][l]\.)(?<![G]\.)(?<=\.|\?)\s", line)
                print("SPLITTED!")
                print(sampleText)

                with open('tokenized_words.txt', 'a') as wf:
                    print("")
                
                    with open('tokenized_words.txt', 'a') as wf:
                        for words in sampleText:
                            print(words)
                            wf.write(words)

                            if (words) == 'Bb':
                                wf.write(".")
                            if (words) == 'Gng':
                                wf.write(".")
                            if (words) == 'Pang':
                                wf.write(".")
                            if (words) == 'Gat':
                                wf.write(".")
                            if (words) == 'hal':
                                wf.write(".")
                            if (words) == 'G':
                                wf.write(".")
                            if (words) == 'A':
                                wf.write(".")
                            if (words) == 'B':
                                wf.write(".")
                            if (words) == 'C':
                                wf.write(".")
                            if (words) == 'D':
                                wf.write(".")
                            if (words) == 'E':
                                wf.write(".")
                            if (words) == 'F':
                                wf.write(".")
                            if (words) == 'H':
                                wf.write(".")
                            if (words) == 'I':
                                wf.write(".")
                            if (words) == 'J':
                                wf.write(".")
                            if (words) == 'K':
                                wf.write(".")
                            if (words) == 'L':
                                wf.write(".")
                            if (words) == 'M':
                                wf.write(".")
                            if (words) == 'N':
                                wf.write(".")
                            if (words) == 'O':
                                wf.write(".")
                            if (words) == 'P':
                                wf.write(".")
                            if (words) == 'Q':
                                wf.write(".")
                            if (words) == 'R':
                                wf.write(".")
                            if (words) == 'S':
                                wf.write(".")
                            if (words) == 'T':
                                wf.write(".")
                            if (words) == 'U':
                                wf.write(".")
                            if (words) == 'V':
                                wf.write(".")
                            if (words) == 'W':
                                wf.write(".")
                            if (words) == 'X':
                                wf.write(".")
                            if (words) == 'Y':
                                wf.write(".")
                            if (words) == 'Z':
                                wf.write(".")
                            wf.write("\n")
                            
                            if (words) == '.':
                                wf.write("\n")
                            
    except:
        print("Failed!")

sentenceNormalizer()
sentenceTokenizer()
wordTokenizer()

