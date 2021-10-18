# -*-coding: UTF-8 -*-
from Bio import SeqIO
from Bio.Seq import Seq
import sys
import random

fasta = sys.argv[1]
number = int(sys.argv[2])

cdsseq_dict = SeqIO.index_db(fasta+'.idx',fasta,'fasta')
total_num = len(cdsseq_dict.keys())
if number > total_num:
    print("The total number of sequences is less than the given value.")
else:
    randseq = random.choices(list(cdsseq_dict.keys()),k=number)
    for i in randseq:
        print(">"+cdsseq_dict[i].id+'\n'+cdsseq_dict[i].seq)
