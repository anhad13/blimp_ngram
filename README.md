# blimp_ngram

Instructions to run:

Follow build instructions from https://github.com/kpu/kenlm. Inside the build folder keep this repo. The .py/.s files of this repo should be directly inside the build folder.

Run build_arpa.s to create the ARPA from a raw file. If using English Giga word, use https://github.com/nelson-liu/flatten_gigaword to create the raw file and change the path in build_arpa.s to point to this.

Once the arpa file is built, run blimp_eval.py to tu run blimp evaluation. Note: the path to the git repo wherein the blimp data is stored has to be changed in this file accordingly.
