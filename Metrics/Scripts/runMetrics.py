import metrics as m
import pandas as pd

metricData = pd.read_csv("/Users/michaelpoblacion/Documents/VCU/Fall19/CMSC435/Protein-Classification/PreProcessing/PFeature/RF_new.csv", sep=';', header=None)
header = metricData.iloc[0]
metricData = metricData[1:]
metricData.columns = header

predictionList = metricData['prediction(Class)'].values.tolist()
trueList = metricData['Class'].values.tolist()

actualPrediction = []
actualTrue = []

for pred in predictionList:
    if pred == 'DNA':
        actualPrediction.append(bin(0))
    elif pred == 'RNA':
        actualPrediction.append(bin(1))
    elif pred == 'DRNA':
        actualPrediction.append(bin(2))
    else:
        actualPrediction.append(bin(3))

for true in trueList:
    if true == 'DNA':
        actualTrue.append(bin(0))
    elif true == 'RNA':
        actualTrue.append(bin(1))
    elif true == 'DRNA':
        actualTrue.append(bin(2))
    else:
        actualTrue.append(bin(3))

metricList = m.generate_metrics(actualPrediction, actualTrue)

for m in metricList:
    print(m)

print("Finished")
