import json
import functools

import et.sent_splitter
import et.sent_tokenizer
import et.pos_tagger
import et.translator
import et.grammar_normalizer

def translate(inp,fh=False):
    inp = sent_splitter.sent_split(inp,fh)
    inp = sent_tokenizer.sent_tokenize_multi(inp,fh)
    inp = pos_tagger.pos_tag_multi(inp,fh)
    inp = translator.translate_multi(inp,fh)
    inp = grammar_normalizer.grammar_normalize_multi(inp,fh)

    ##########################################
    inp = " ".join([" ".join([i[0] for i in sentence]) for sentence in inp])
    if fh:
        file = open("et/data/temp/__init__.json","w")
        file.write(json.dumps(inp,indent=4))
        file.close()
    return inp

if __name__=="__main__":
    #data = "The dog is cute. Hello Mr. Nigga Z. Bluem-Blum! The Monkey climb the wall."
    data = "Good morning. It is a sunny day. Tomorrow is Tuesday. I am happy today."
    print(translate(data,True))
