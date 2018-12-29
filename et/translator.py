'''
Person in Charge::
Programmer:
	Owera
	Lascano
	Manalo
Researcher:
	Collado
Documentor:
	Galapin

<Put your description/documentation here.>
'''
import sqlite3
import json

def translate_multi(inp,fh=False):
	ans = []
	for i in inp:
		ans.append(translate(i))
	if fh:
		file = open("et/data/temp/translator.json","w")
		file.write(json.dumps(ans,indent=4))
		file.close()
	return ans
	
def translate(wordTagged,fh=False):
	candidates = _get_word_candidates(wordTagged)
	scores = _score(candidates)
	winners=[]
	for i in range(len(scores)):
		index = scores[i].index(max(scores[i]))
		winners.append((candidates[i][index],wordTagged[i][1]))
	if fh:
		file = open("et/data/temp/translator.json","w")
		file.write(json.dumps(winners,indent=4))
		file.close()
	return winners

def _get_word_candidates(inp):
	conn = sqlite3.connect("et/data/database.db")
	cursor = conn.cursor()
	ans = []
	for i in inp:
		word = i[0]
		temp = cursor.execute("SELECT word.name FROM word WHERE langId=0 and word.id in(SELECT idTranslation FROM translation where idword in (SELECT word.id FROM word WHERE word.name like ? and langId=1))",[word]).fetchall()
		temp = [i[0] for i in temp] if temp else [word]
		ans.append(temp)
	conn.close()
	return ans
def _score(inp):
	ans = []
	inp_len = len(inp)
	for row in range(inp_len):
		voters = _get_voters(inp,row)
		candidates = inp[row]
		grp_score = []
		for candidate in candidates:
			temp_score=0
			for m in voters:
				for n in m:
					temp_score+=_get_score(candidate,n)
			grp_score.append(temp_score)
		ans.append(grp_score)
	return ans

def _get_score(candidate,voter):
	conn = sqlite3.connect("et/data/alt.db")
	cursor = conn.cursor()
	ans = cursor.execute("SELECT COUNT(*) FROM sentences WHERE sentence like ? and sentence like ?",["% "+candidate+" %","% "+voter+" %"]).fetchall()[0][0]
	conn.close()
	return ans
def _get_voters(inp,index):
	ans = [] if index<=0 else inp[:index]
	ans += [] if index>=len(inp) else inp[index+1:]
	return ans
if __name__=="__main__":
	#inp = [["The","ART"],["bat","NN"],["is","LV"],["hard","ADJ"]]
	inp = [["I","NNP"],["will","VBP"],["climb","VB"],["the","DET"],["banana","NN"],["tree","NN"]]
	print(translate(inp,True))
