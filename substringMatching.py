import pandas as pd


def findSubstrings(dataframe, length):
    index = 0
    substringList = pd.DataFrame(columns=['Sequence Index', 'Substring'])
    for x in range(len(dataframe.index) - 1):
        stringOne = dataframe.iat[x, 0]
        stringTwo = dataframe.iat[x+1, 0]
        possSubstring = ''
        i = 0
        j = 0
        oneMax = len(stringOne)
        twoMax = len(stringTwo)
        while i < oneMax:
            if j == twoMax:
                j = 0
                i = i + 1
            elif stringOne[i] == stringTwo[j]:
                possSubstring = possSubstring + stringOne[i]
                i = i + 1
                j = j + 1
            elif stringOne[i] != stringTwo[j]:
                if len(possSubstring) >= length:
                    if possSubstring not in substringList:
                        data = pd.DataFrame({'Sequence Index': x, 'Substring': possSubstring}, index=[index])
                        substringList = substringList.append(data)
                        index = index + 1
                    possSubstring = ''
                    i = i + 1
                    j = 0
                elif len(possSubstring) < length:
                    j = j + 1
        if len(possSubstring) > 0 and possSubstring not in substringList:
            data = pd.DataFrame({'Sequence Index': x, 'Substring': possSubstring}, index=[index])
            substringList = substringList.append(data)
            index = index + 1
    return substringList


def scoreSubstrings(dataframe, substrings):
    scoreList = pd.DataFrame(columns=['Sequence', 'Substring', 'Count'])
    index = 0
    for row in dataframe.iterrows():
        sequence = row[1]['Sequence']
        for y in range(len(substrings.index) - 1):
            string = substrings.iat[y, 1]
            score = 0
            i = 0
            j = 0
            iMax = len(row[1]['Sequence'])
            jMax = len(string)
            while i < iMax:
                if j >= jMax:
                    i = i + 1
                    j = 0
                elif sequence[i] != string[j]:
                    j = j + 1
                elif sequence[i] == string[j]:
                    i = i + 1
                    j = j + 1
                    if j == jMax:
                        score = score + 1
                        j = 0
            data = pd.DataFrame({'Sequence': sequence, 'Substring': string, 'Count': score}, index=[index])
            scoreList = scoreList.append(data)
            index = index + 1
    return scoreList


def saveScoreFrames(dataframe, proteinType):
    dataframe.to_csv('ProteinScore' + proteinType + str(substringLength) + '.csv')


def saveSubstrings(substrings, proteinType):
    substrings.to_csv('ProteinSubstring' + proteinType + str(substringLength) + '.csv')


def separateDataframe(dataframe, identifier):
    newFrame = pd.DataFrame(columns=['Sequence'])
    count = 0
    for x in range(len(dataframe.index)):
        if dataframe.iat[x, 1] == identifier:
            data = pd.DataFrame({'Sequence': dataframe.iat[x, 0]}, index=[count])
            newFrame = newFrame.append(data)
            count = count + 1
    return newFrame


trainingData = pd.read_csv('CMSC435TrainingDataset.txt',
                           sep=',', header=None, names=['Sequence', 'Class'])

proteinClass = 'DRNA'
substringLength = 3

classFrame = separateDataframe(trainingData, proteinClass)
classSubstrings = findSubstrings(classFrame, substringLength)
saveSubstrings(classSubstrings, proteinClass)
classScore = scoreSubstrings(classFrame, classSubstrings)
saveScoreFrames(classScore, proteinClass)

# DNAFrame = separateDataframe(trainingData, 'DNA')
# RNAFrame = separateDataframe(trainingData, 'RNA')
# DRNAFrame = separateDataframe(trainingData, 'DRNA')
# NonDRNAFrame = separateDataframe(trainingData, 'nonDRNA')

# DNASubstrings = findSubstrings(DNAFrame)
# saveSubstrings(DNASubstrings, 'DNA')

# RNASubstrings = findSubstrings(RNAFrame)
# saveSubstrings(RNASubstrings, 'RNA')

# DRNASubstrings = findSubstrings(DRNAFrame)
# saveSubstrings(DRNASubstrings, 'DRNA')

# NonDRNASubstrings = findSubstrings(NonDRNAFrame)
# saveSubstrings(NonDRNASubstrings, 'NonDRNA')

# DNAScore = scoreSubstrings(DNAFrame, DNASubstrings)
# saveScoreFrames(DNAFrame, 'DNA')

# RNAScore = scoreSubstrings(RNAFrame, RNASubstrings)
# saveScoreFrames(RNAFrame, 'RNA')

# DRNAScore = scoreSubstrings(DRNAFrame, DRNASubstrings)
# saveScoreFrames(DRNAScore, 'DRNA')

# NonDRNAScore = scoreSubstrings(NonDRNAFrame, NonDRNASubstrings)
# saveScoreFrames(NonDRNAFrame, 'NonDRNA')
