#############################################################
# Author : Michael Poblacion
# Date : 10/27/2019
# Description: A script for SMOTE on datasets
#
# NOTE: Readme available for instructions to set up for RapidMiner
#
# NOTE: 'CONST_CLASS_LABEL' may need to change depending on your dataset "class column name"
#############################################################

from collections import Counter
from imblearn.combine import SMOTETomek
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

CONST_CLASS_LABEL = "[Class]"
#Default method called by
def rm_main(data):
    column_vals = data.columns
    X = np.array(data.loc[:, data.columns != CONST_CLASS_LABEL]) # All of the features into an np array
    y = np.array(data.loc[:, data.columns == CONST_CLASS_LABEL]) # The class into an np array
    smt = SMOTETomek(random_state=2) #performs SMOTE and TOMEK
    #For SMOTE only.. use SMOTE(random_state=2)
    feature_train_res, class_train_res = smt.fit_sample(X, y.ravel()) # performs SMOTE
    full_training_set = np.column_stack((feature_train_res,class_train_res))
    df = pd.DataFrame(data=full_training_set, columns = column_vals)
    return df
