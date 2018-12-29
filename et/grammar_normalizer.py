import json
from pathlib import Path as path

def read_input():
    with open("et/data/temp/translator.json") as json_file:
        _input = json.load(json_file)
    return _input
    

def grammar_normalize_multi(multi, fh=False):
    ans = []
    for i in multi:
        sentence = grammar_normalize(i)
        for entity in sentence:
            ans.append(entity)
    if fh:
        file = open('et/data/temp/grammar_normalizer.json', 'w')
        file.write(json.dumps(ans, indent=4))
        file.close()
    return ans

def grammar_normalize(single, fh=False):
    ans = []
    grammarrules = read_grammar_rule()
    ans.append(grammar_check(single, grammarrules))
    ##ans.append(normalize(grammar_check(single, grammarrules),grammarrules))
    if fh:
        file = open('et/data/temp/grammar_normalizer.json', 'w')
        file.write(json.dumps(ans, indent=4))
        file.close()
    return ans

def grammar_check(single, grammarrules):
    output = []
    sentencegrammar = ''
    for word in single:
        sentencegrammar = sentencegrammar + word[1]
        if(not 'PRD' in word):
            sentencegrammar = sentencegrammar + ' '
    if(not sentencegrammar in grammarrules):
        newsentence = normalize(single, sentencegrammar, grammarrules)
    for entity in newsentence:
        output.append(entity)
    return output

def normalize(single, sentencegrammar, grammarrules):
    newsentence = []
    learnnewgrammar = False
    for rule in grammarrules:
        grammarplacing = False
        ruleattrib = rule[0].split()
        sentencegrammarattrib = sentencegrammar.split()

        allattribin = False
        for attrib in ruleattrib:
            if(attrib in sentencegrammarattrib):
                allattribin = True
            else:
                allattribin = False
                break
        if(allattribin):
            learnnewgrammar = False
            for attrib in ruleattrib:
                for entity in sentence:
                    if(attrib in entity):
                        newsentence.append(entity)
            break
        else:
            learnnewgrammar = True
    if(learnnewgrammar):
        for entity in single:
            newsentence.append(entity)
        learn_grammar_rule(sentencegrammar, grammarrules)

    return newsentence

def read_grammar_rule():
    grammarrules = []
    with open("et/data/grammar_normalizer_data/grammar_rules.json") as json_file:
        grammarrules = json.load(json_file)
    return grammarrules

def read_occurence_grammar():
    with open('et/data/grammar_normalizer_data/grammar_learning.json') as json_file:
        occurence = json.load(json_file)
    return occurence

def learn_grammar_rule(sentencegrammar, grammarrules):
    occurence = []
    
    if(path('et/data/grammar_normalizer_data/grammar_learning.json').exists()):
        occurencegrammar = read_occurence_grammar()
        for entity in occurencegrammar:
            occurence.append(entity)
    newoccurence = []
    if(len(occurence) is 0):
        newoccurence.append(sentencegrammar)
        newoccurence.append('1')
        occurence.append(newoccurence)
    else:
        ingrammarrules = False
        x = 0
        for rule in occurence:
            if(sentencegrammar in rule[0]):
                count = int(rule[1])
                count = count + 1
                occurence[x][1] = str(count)
                if(count == 50):
                    grammarrules.append(rule[0])
                    refresh_grammar_rule(grammarrules)
                ingrammarrules = True
            x = x + 1
        if(not ingrammarrules):
            newoccurence.append(sentencegrammar)
            newoccurence.append('1')
            occurence.append(newoccurence)            
        pass
    file = open('et/data/grammar_normalizer_data/grammar_learning.json','w')
    file.write(json.dumps(occurence,indent=4))
    file.close()

def refresh_grammar_rule(grammarrules):
    file = open('et/data/grammar_normalizer_data/grammar_rules.json','w')
    file.write(json.dumps(grammarrules,indent=4))
    file.close()
    
if __name__ == '__main__':
    data = read_input()
    #print(data[0][0][0])
    #print(grammar_normalize(data[0], True))
    print(grammar_normalize_multi(data, True))
