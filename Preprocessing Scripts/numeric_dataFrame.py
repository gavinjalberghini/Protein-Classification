#############################################################
# Author : Michael Poblacion
# Date : 11/3/2019
# Description: A script for turning dataset to numeric for  proper matching
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
    full_training_set = np.column_stack((X,y))
    df = pd.DataFrame(data=full_training_set, columns = column_vals)
    df["[Class]"].replace(['DNA', 'DRNA', 'nonDRNA'], ["No", "No", "No"], inplace=True)
    df["[Class]"].replace(['RNA'], ["Yes"], inplace=True)
    return df
