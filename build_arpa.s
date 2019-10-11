#!/bin/bash
#
#SBATCH -t48:00:00
#SBATCH --mem=200GB
#SBATCH --nodes=1
#SBATCH --gres=gpu:1

bin/lmplz -o 5 -S 80% -T  /misc/vlgscratch4/BowmanGroup/anhad/kenlm/build  --text ../../etc/EnglishGigaWordCorpus/data/egw.full > egw.arpa
