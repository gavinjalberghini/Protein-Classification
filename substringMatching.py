import pandas as pd


def findSubstrings(dataframe, length):
    index = 0
    substringList = pd.DataFrame(columns=['Sequence Index', 'Substring'])
    for x in range(len(dataframe.index) - 1):
        for y in range(x, len(dataframe.index) - 1):
            stringOne = dataframe.iat[x, 0]
            stringTwo = dataframe.iat[y, 0]
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
                        if not substringInList(substringList, possSubstring):
                            data = pd.DataFrame({'Sequence Index': x, 'Substring': possSubstring}, index=[index])
                            substringList = substringList.append(data)
                            index = index + 1
                        possSubstring = ''
                        i = i + 1
                        j = 0
                    elif len(possSubstring) < length:
                        j = j + 1
                        possSubstring = ''
        if len(possSubstring) >= length and not substringInList(substringList, possSubstring):
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
            if not substringInList(scoreList, string):
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


def getFrequentSubstrings(scoreFrame):
    scoreFrame = scoreFrame.sort_values(by='Count', ascending=False)
    frequentDF = pd.DataFrame(columns=['Substring', 'Count'])
    for count in range(0, frequentSubstringLength):
        sub = scoreFrame.iat[count, 1]
        num = scoreFrame.iat[count, 2]
        if not substringInList(frequentDF, sub):
            data = pd.DataFrame({'Substring': sub, 'Count': num}, index=[count])
            frequentDF = frequentDF.append(data)
    return frequentDF


def printFrequentSubstrings(frame):
    for row in frame.iterrows():
        sub = row[1]['Substring']
        num = row[1]['Count']
        print('Substring ' + sub + ' appeared in class ' + proteinClass + ' ' + str(num) + ' times')


def substringInList(dataframe, string):
    for row in dataframe.iterrows():
        compString = row[1]['Substring']
        if string == compString:
            return True
    return False


trainingData = pd.read_csv('CMSC435TrainingDataset.txt',
                           sep=',', header=None, names=['Sequence', 'Class'])

proteinClass = 'DNA'
substringLength = 5
frequentSubstringLength = 10

classFrame = separateDataframe(trainingData, proteinClass)

classSubstrings = findSubstrings(classFrame, substringLength)
saveSubstrings(classSubstrings, proteinClass)

classScore = scoreSubstrings(classFrame, classSubstrings)
saveScoreFrames(classScore, proteinClass)

mostFrequentSubstrings = getFrequentSubstrings(classScore)
mostFrequentSubstrings.to_csv('MostFrequentSubstrings' + proteinClass + str(frequentSubstringLength) + '.csv')
printFrequentSubstrings(mostFrequentSubstrings)
