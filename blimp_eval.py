import os
import json
import kenlm
import re
import spacy
en_nlp = spacy.load("en")
import numpy as np
model = kenlm.Model('egw.arpa')
if __name__ == '__main__':
	arr = []
	for root, dirs, files in os.walk("/misc/vlgscratch4/BowmanGroup/anhad/ngrm/data_generation/outputs/benchmark/"):
		for name in files:
			if "jsonl" not in name:
				continue
			print(name)
			f = open(os.path.join(root, name))
			lines = f.readlines()
			correct = 0
			total = 0
			for l in lines:
				l = json.loads(l)
				bads = " ".join([str(x) for x in en_nlp.tokenizer(re.sub(r"\n+", "\n", l['sentence_bad']).replace("\n"," "))])#;print(bads)
				goods = " ".join([str(x) for x in en_nlp.tokenizer(re.sub(r"\n+", "\n", l['sentence_good']).replace("\n"," "))])
				bp = model.score(bads, bos = False, eos = False)
				gp = model.score(goods, bos = False, eos = False)
				if gp > bp:
        				correct+=1
				total+=1
			print(str(correct)+" / "+str(total))
			arr.append(correct)
	print("Final results: " + str(np.average(arr)))
