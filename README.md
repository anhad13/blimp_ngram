# blimp_ngram

Instructions to run:

Follow build instructions from https://github.com/kpu/kenlm. Inside the build folder keep this repo. The .py/.s files of this repo should be directly inside the build folder.

Run build_arpa.s to create a .arpa file from the raw text file. The .arpa file contains entire 1-n grams stored in a searchable format. If using English Gigaword, use https://github.com/nelson-liu/flatten_gigaword to create the raw file and change the path (--text) build_arpa.s (line 8) to point to this.

Once the arpa file is built, run blimp_eval.py to tu run blimp evaluation. Note: the path to the git repo wherein the blimp data is stored has to be changed in this file accordingly.
