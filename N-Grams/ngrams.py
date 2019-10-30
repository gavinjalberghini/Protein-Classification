import pandas as pd
import itertools as iter
import time
#A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y
#Intended only for the creation of functions, please run ngrams_metrics for cleaning

def csv_export(origin, df):
    row = 0
    for string in origin[0]:
        for c in combos:
            df[c].iloc[row] = string.count(c)
        row = row+1

chars = 'ACDEFGHIKLMNPQRSTVWY'
combos = []
for x in list(iter.combinations_with_replacement(chars, 2)):
    combos.append(''.join(x))

dna = pd.read_csv("data/435DNAOnly.csv", header=None)
rna = pd.read_csv("data/435RNAOnly.csv", header=None)
drna = pd.read_csv("data/435DRNAOnly.csv", header=None)
ndrna =  pd.read_csv("data/435NDRNAOnly.csv", header=None)

dfdna = pd.DataFrame(0, index=range(len(dna)), columns=combos)
dfrna = pd.DataFrame(0, index=range(len(rna)), columns=combos)
dfdrna = pd.DataFrame(0, index=range(len(drna)), columns=combos)
dfndrna = pd.DataFrame(0, index=range(len(ndrna)), columns=combos)

print("csv export dna {0}".format(time.time()))
csv_export(dna, dfdna)
print("csv export rna {0}".format(time.time()))
csv_export(rna, dfrna)
print("csv export drna {0}".format(time.time()))
csv_export(drna, dfdrna)
print("csv export ndrna {0}".format(time.time()))
csv_export(ndrna, dfndrna)
print("finished csv export {0}".format(time.time()))

dfdna.to_csv("2-grams_dna.csv")
dfrna.to_csv("2-grams_rna.csv")
dfdrna.to_csv("2-grams_drna.csv")
dfndrna.to_csv("2-grams_ndrna.csv")
