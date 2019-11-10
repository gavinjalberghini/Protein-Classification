#############################################################
# Author : Michael Poblacion
# Date : 10/27/2019
# Description: A script for SMOTE on datasets
#
# NOTE: To use, pass in arguments
#               1. file name/path to smote
#               2. file name of new csv
#       Example: python SampleBalancerNonRapidMiner.py fileToSmote.csv trainingset.csv
# NOTE: The 'CONST_CLASS_LABEL' variable may need to be renamed depending
#       on the attribute name.
#
# OUTPUT: csv file with smote and tomek performed
#############################################################

from collections import Counter
from imblearn.combine import SMOTETomek
import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

CONST_CLASS_LABEL = "[Class]"

file_to_smote = sys.argv[1]
train_csv_name = sys.argv[2]

# Convert dataframe entries to floats
def turn_to_float(df):
    for col in df.columns:
        if(col != CONST_CLASS_LABEL):
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# Read file, turn features to floats, return dataset
def read_data(file):
    dataset = pd.read_csv(file)
    #TODO: Once features are turned into measurable numbers, uncomment line below
    #dataset = turn_to_float(dataset)
    return dataset

# Saves dataset to csv
def save_csv(dataset, name_of_file):
     with open(name_of_file, "w") as output:
         writer = csv.writer(output, lineterminator='\n')
         for val in full_training_set:
             writer.writerow([val])

dataset = pd.read_csv(file_to_smote)
dataset = dataset.fillna(dataset.mean())
column_vals = dataset.columns
X = np.array(dataset.loc[:, dataset.columns != CONST_CLASS_LABEL]) # All of the features into an np array
y = np.array(dataset.loc[:, dataset.columns == CONST_CLASS_LABEL]) # The class into an np array

#feature_train, X_test, class_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0) # split into training and testing set.

smt = SMOTETomek(random_state=2) #performs SMOTE and TOMEK
#For SMOTE only.. use SMOTE(random_state=2)

feature_train_res, class_train_res = smt.fit_sample(X, y.ravel()) # performs SMOTE


full_training_set = np.column_stack((feature_train_res,class_train_res))

df = pd.DataFrame(data=full_training_set, columns = column_vals)

df.to_csv(train_csv_name, index=False)
print("CSV '"+ train_csv_name + "' saved in directory")
#NOTE: SMOTENC can handle categorical features
