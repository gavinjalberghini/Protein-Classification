######
# Author: Mike F
# Date: 10/25/2019
# Description:
######

import pandas as pd


# Arguments:
# Dataframe - a pandas dataframe generated from an CSV file
# length - the minimum length the substring must match or exceed to be added to the collection
#
# Returns a pandas dataframe with all substrings that appeared
# This function will go through every sequence in the dataframe and check each character in that sequence against
# the characters of all other sequences
# O(n^2) complexity, this will run poorly against large dataframes when the length is low
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


# Goes through the collection of the substrings found, and sees how many times that substring has appeared in the
# Original dataframe, returns a dataframe with the row, substring, and the count
def scoreSubstrings(dataframe, substrings):
    scoreList = pd.DataFrame(columns=['Sequence', 'Substring', 'Count'])
    index = 0
    scoreThreshold = len(dataframe.index) / scoreLength
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
            if not substringInList(scoreList, string) and score >= scoreThreshold:
                data = pd.DataFrame({'Sequence': sequence, 'Substring': string, 'Count': score}, index=[index])
                scoreList = scoreList.append(data)
                index = index + 1
    return scoreList


# Saves the score file to CSV
def saveScoreFrames(dataframe, proteinType):
    dataframe.to_csv('Data/ProteinScore' + proteinType + str(substringLength) + '.csv')


# Saves the substring file to CSV
def saveSubstrings(substrings, proteinType):
    substrings.to_csv('Data/ProteinSubstring' + proteinType + str(substringLength) + '.csv')


# This will take the initial dataframe, and only return the rows that have the correct class
def separateDataframe(dataframe, identifier):
    newFrame = pd.DataFrame(columns=['Sequence'])
    count = 0
    for x in range(len(dataframe.index)):
        if dataframe.iat[x, 1] == identifier:
            data = pd.DataFrame({'Sequence': dataframe.iat[x, 0]}, index=[count])
            newFrame = newFrame.append(data)
            count = count + 1
    return newFrame


# Returns a dataframe that has the top % of substrings based on their count
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


# Prints out the frequent substrings
def printFrequentSubstrings(frame):
    for row in frame.iterrows():
        sub = row[1]['Substring']
        num = row[1]['Count']
        print('Substring ' + sub + ' appeared in class ' + proteinClass + ' ' + str(num) + ' times')


# Checks to see if the substring already exists in a dataframe
def substringInList(dataframe, string):
    for row in dataframe.iterrows():
        compString = row[1]['Substring']
        if string == compString:
            return True
    return False


trainingData = pd.read_csv('CMSC435TrainingDataset.txt', sep=',', header=None, names=['Sequence', 'Class'])

# This block will be the configurable portion for the user
# proteinClass will be of the choices "DNA, RNA, DRNA, or nonDRNA"
# substringLength will be the minimum length of a potential substring to be added to the dataframe
# frequentSubstringLength is the number of frequent substrings you are looking to be outputted
# scoreLength will be the number that divides the length of the imported dataframe by the chosen class
# so if the dataframe rows is 2000, it'll only add substrings that have a count of 200/ scoreLength
proteinClass = 'DNA'
substringLength = 10
frequentSubstringLength = 10
scoreLength = 10

classFrame = separateDataframe(trainingData, proteinClass)

classSubstrings = findSubstrings(classFrame, substringLength)
saveSubstrings(classSubstrings, proteinClass)

classScore = scoreSubstrings(classFrame, classSubstrings)
saveScoreFrames(classScore, proteinClass)

mostFrequentSubstrings = getFrequentSubstrings(classScore)
mostFrequentSubstrings.to_csv('Data/MostFrequentSubstrings' + proteinClass + str(frequentSubstringLength) + '.csv')
printFrequentSubstrings(mostFrequentSubstrings)
