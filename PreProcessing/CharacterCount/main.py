import pandas as pd


def countString(comp, sequence):
    count = 0
    for char in sequence:
        if char == comp:
            count = count + 1
    return count


# Read the dataset
trainingData = pd.read_csv('../CMSC435TrainingDataset.txt',
                           sep=',', header=None, names=['Sequence', 'Class'])
# Save the
trainingData.to_csv('CMSC435TrainingData.csv')
# Define the testString used against the dataset
testStrings = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'K', 'L', 'M', 'N', 'P', 'Q', 'R',
               'S', 'T', 'V', 'W', 'Y']

# Define the columns used in the new Dataset
columns = ['Row', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'K', 'L', 'M', 'N', 'P', 'Q', 'R',
           'S', 'T', 'V', 'W', 'Y', 'Class']

newDataset = pd.DataFrame(columns=columns)

# Fill new Dataset with the information
newCount = 0
for row in trainingData.iterrows():
    newDataset = newDataset.append({'Row': newCount, 'Class': row[1]['Class']}, ignore_index=True)
    for string in testStrings:
        charCount = countString(string, row[1]['Sequence'])
        newDataset.set_value(newCount, string, charCount)
    newCount = newCount + 1

# Export the dataset into a file
newDataset.to_csv('ProjectTest.csv')

numRows = len(newDataset.index)
numCol = len(newDataset.columns)

for x in range(0, numRows):
    highestVal = 0
    highestCol = ''
    for y in range(1, numCol-1):
        if int(newDataset.iat[x, y]) > highestVal:
            highestVal = newDataset.iat[x, y]
            highestCol = newDataset.columns[y]
    print("The greatest value for row " + str(x) + " is " + str(highestVal) + " at column " + highestCol)
