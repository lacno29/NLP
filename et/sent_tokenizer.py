"""
Author: Marion Owera
Date Written: Feb 25, 2018
Description: Temporary sent_tokenizer lang to, may problema pa kasi dun sa tokenizer ni Jeremy.
"""

import re
import json

def sent_tokenize(inp,fh=False):
    sym =r"([,\"\'])"
    inp = re.sub(r"(\w+)"+sym+r"(\w+)"+sym+r"(\w+)",r"\1 \2 \3 \4 \5",inp)
    inp = re.sub(r"(\w+)"+sym+r"(\w+)",r"\1 \2 \3",inp)
    inp = re.sub(sym+r"(\w+)",r"\1 \2",inp)
    inp = re.sub(r"(\w+)"+sym,r"\1 \2",inp)
    inp = re.sub(r"(\w+)(\W)$",r"\1 \2",inp)
    inp = inp.split()
    if fh:
        file = open("et/data/temp/sent_tokenizer.json","w")
        file.write(json.dumps(inp,indent=4))
        file.close()
    return inp

def sent_tokenize_multi(inp,fh=False):
    ans = []
    for i in inp:
        ans.append(sent_tokenize(i))
    if fh:
        file = open("et/data/temp/sent_tokenizer.json","w")
        file.write(json.dumps(ans,indent=4))
    return ans


if __name__=="__main__":
    print(sent_tokenize_multi(["Banana,Mango,Apple2,etc. I like them all, but, it's bad.","The dog is cute!"],True))
