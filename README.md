# blimp_ngram

Instructions to run BLiMP on n-gram:

Download the BLiMP data: https://github.com/alexwarstadt/blimp

Follow build instructions from https://github.com/kpu/kenlm. Inside the build folder keep this repo. The .py/.s files of this repo should be directly inside the build folder.

Run build_arpa.s to create a .arpa file from the raw text file. The .arpa file contains entire 1-n grams stored in a searchable format. If using English Gigaword, use https://github.com/nelson-liu/flatten_gigaword to create the raw file and change the path (--text) build_arpa.s (line 8) to point to this. Also, alter line 11 of build_arpa.py to point to the location where BLiMP data is located.

Once the arpa file is built (it might take a couple of hours!), run blimp_eval.py to tu run BLiMP evaluation.

