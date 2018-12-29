from .textblob import TextBlob
from .gap import PerceptronTagger
import json

def pos_tag(text,fh=False):
    assert type(text) == list, "Input must be a list!!!"
    wordTagged = _tagPunctuations(_pos_tag(text))
    assert type(wordTagged) == list, "wordTagged must be a list!!!"
    for wordtag_tuple in wordTagged:
        assert type(wordtag_tuple == tuple), "{0} must be a tuple".format(wordtag_tuple)
        for item in wordtag_tuple:
            assert type(item == str), "{0} must be a str".format(item)
    if fh:
        file = open('et/data/temp/pos_tagger.json', 'w')
        file.write(json.dumps(wordTagged, indent=4))
        file.close()
    return wordTagged

def pos_tag_multi(sentences, fh=False):
    ans=list(map(lambda sentence: pos_tag(sentence), sentences))
    if fh:
        file = open('et/data/temp/pos_tagger.json', 'w')
        file.write(json.dumps(ans, indent=4))
        file.close()
    return ans

def _pos_tag(text):
    sentence = ' '.join(text)
    blob = TextBlob(sentence, pos_tagger = PerceptronTagger())
    return blob.tags

def _tagPunctuations(tags):
    tags = [[x, y] for (x,y) in tags]
    for tagged_word in tags:
            if tagged_word[0] == '.':
                tagged_word[1] = 'PRD'
            elif tagged_word[0] == '!':
                tagged_word[1] = 'EXC'
            elif tagged_word[0] == '?':
                tagged_word[1] = 'QUE'
            elif tagged_word[0] == ',':
                tagged_word[1] = 'COM'
            elif tagged_word[0] == '"':
                tagged_word[1] = 'QUO'
            elif tagged_word[0] == ':':
                tagged_word[1] = 'COL'
            elif tagged_word[0] == ';':
                tagged_word[1] = 'SEM'
    tags = [(x, y) for [x,y] in tags]
    return tags
