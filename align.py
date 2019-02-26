#writing a script that will align a given sequence with the B. subtilis 168 
#genome and find the position of the sequence on the genome

from Bio import SeqIO
import gzip

genome_file = raw_input("Genome genbank (gzip) file name: ")

with gzip.open("~/" + genome_file)

genome = SeqIO.open()