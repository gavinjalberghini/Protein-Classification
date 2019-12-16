######
# Author: Mike F
# Date: 10/25/2019
# Description: A script used to pipe information to the metrics script
######

import metrics as m
import pandas as pd

CONST_IN_PATH = ""
CONST_OUT_PATH = ""

metricData = pd.read_csv(CONST_IN_PATH, sep=';', header=None)
header = metricData.iloc[0]
metricData = metricData[1:]
metricData.columns = header

predictionList = metricData['prediction(Class)'].values.tolist()
trueList = metricData['Class'].values.tolist()

prediction = []
actual = []

print("Fetching metric data... ")
for pred in predictionList:
    if pred == 'DNA':
        prediction.append(bin(0))
    elif pred == 'RNA':
        prediction.append(bin(1))
    elif pred == 'DRNA':
        prediction.append(bin(2))
    else:
        prediction.append(bin(3))

for true in trueList:
    if true == 'DNA':
        actual.append(bin(0))
    elif true == 'RNA':
        actual.append(bin(1))
    elif true == 'DRNA':
        actual.append(bin(2))
    else:
        actual.append(bin(3))

metricList = m.generate_metrics(prediction, actual)

print("Printing...")
for m in metricList:
    print(m)

print("Done.")
