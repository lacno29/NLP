'''
Person in Charge::
Programmer:
	Emer Cruz
	Marion Z. Owera
Researcher: None
Documentor:
	Calinao
	Pena

<Put your description/documentation here.>
Legend:
\\ Slash
\1 Period
'''
import re
import json
import sqlite3
import io

def sent_split(text,fh=False):
	if type(text)==io.TextIOWrapper:
		content = text.read()
		text.close()
		text = content
	assert (type(text)==str),"Input must be a string!!!"
	text = _make_slash_escapable(text)
	text = _make_db_dependent_abbreviation_safe(text)
	text = _make_initial_safe(text)
	text = _make_abbreviation_safe(text)
	text = _preserve_some_mark(text)
	text = _split_text(text)
	text = _make_punc_normal(text)
	text = list(filter(lambda x:x!="",text))
	if fh:
		file=open("et/data/temp/sent_splitter.json","w")
		file.write(json.dumps(text,indent=4))
		file.close()
	return text

def _make_slash_escapable(text):
	return re.sub(r"\\",r"\\4",text)
def _make_db_dependent_abbreviation_safe(text):
	conn = sqlite3.connect("et/data/abbrev.db")
	cursor = conn.cursor()
	res = cursor.execute("SELECT DISTINCT abbrev FROM abbreviation").fetchall()
	conn.close()
	for i in res:
		i=i[0]
		to = re.sub(r"[.]",r"\\\\0",i)
		text = re.sub(r"(\W|^)"+re.escape(i)+r"(\s)",r"\1"+to+r"\2",text)
	return text
def _make_initial_safe(text):
	return re.sub(r"([A-Z])[.]",r"\1\\0",text)
def _make_abbreviation_safe(text):
	ans = re.sub(r"([A-Za-z0-9_]+)[.]([A-Za-z0-9_]+)[.]([A-Za-z0-9_]+)",r"\1\\0\2\\0\3",text)
	ans = re.sub(r"([A-Za-z0-9_]+)[.]([A-Za-z0-9_]+)",r"\1\\0\2",ans)
	return ans
def _preserve_some_mark(text):
	text = re.sub(r"[.]",r"\\0.",text)
	text = re.sub(r"[!]",r"\\1!",text)
	text = re.sub(r"[?]",r"\\2?",text)
	return text
def _split_text(text):
	text = re.split(r"[.!?]",text)
	return text
def _make_punc_normal(text):
	text = list(map(lambda x:re.sub(r"\\0",r".",x),text))
	text = list(map(lambda x:re.sub(r"\\1",r"!",x),text))
	text = list(map(lambda x:re.sub(r"\\2",r"?",x),text))
	text = list(map(lambda x:re.sub(r"\\4",r"\\",x),text))
	return text
if __name__=="__main__":
	output=sent_split("Dr. MarielDr. C. Congo Came home\\123.0.0.1 3.14 google.me U.S.A. Come Mr. .az Home Baby. Oh my God!!! Do you see that?",True)
	print(output)
