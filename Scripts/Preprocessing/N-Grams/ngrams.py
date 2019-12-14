import pandas as pd
import numpy as np
import itertools as iter
import time
# A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y
# Intended only for the creation of functions, please run ngrams_metrics for cleaning


def csv_export(origin, df):
    row = 0
    for string in origin:
        col = 0
        for c in combos:
            df[row][col] = string.count(c)
            col=col+1
        row = row+1


chars = 'ACDEFGHIKLMNPQRSTVWY'
combos = []

# replace '2' here for more grams
for x in list(iter.combinations_with_replacement(chars, 5)):
    combos.append(''.join(x))

dna = pd.read_csv("data/435DNAOnly.csv", header=None).iloc[:,0].to_numpy()
rna = pd.read_csv("data/435RNAOnly.csv", header=None).iloc[:,0].to_numpy()
drna = pd.read_csv("data/435DRNAOnly.csv", header=None).iloc[:,0].to_numpy()
ndrna =  pd.read_csv("data/435NDRNAOnly.csv", header=None).iloc[:,0].to_numpy()

dfdna = pd.DataFrame(0, index=range(len(dna)), columns=combos).to_numpy()
dfrna = pd.DataFrame(0, index=range(len(rna)), columns=combos).to_numpy()
dfdrna = pd.DataFrame(0, index=range(len(drna)), columns=combos).to_numpy()
dfndrna = pd.DataFrame(0, index=range(len(ndrna)), columns=combos).to_numpy()

# print("csv export dna {0}".format(time.time()))
# csv_export(dna, dfdna)
# dfdna = pd.DataFrame(data=dfdna, columns=combos)
# dfdna.to_csv("2-grams_dna.csv")
# print("finished csv export {0}".format(time.time()))
#
# print("csv export rna {0}".format(time.time()))
# csv_export(rna, dfrna)
# dfrna = pd.DataFrame(data=dfrna, columns=combos)
# dfrna.to_csv("2-grams_rna.csv")
# print("finished csv export {0}".format(time.time()))
#
# print("csv export drna {0}".format(time.time()))
# csv_export(drna, dfdrna)
# dfdrna = pd.DataFrame(data=dfdrna, columns=combos)
# dfdrna.to_csv("2-grams_drna.csv")
# print("finished csv export {0}".format(time.time()))

print("csv export ndrna {0}".format(time.time()))
csv_export(ndrna, dfndrna)
dfndrna = pd.DataFrame(data=dfndrna, columns=combos)
dfndrna.to_csv("5-grams_ndrna.csv")
print("finished csv export {0}".format(time.time()))

