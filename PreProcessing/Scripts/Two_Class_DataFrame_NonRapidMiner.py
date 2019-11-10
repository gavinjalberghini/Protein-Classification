#############################################################
# Author : Michael Poblacion
# Date : 10/30/2019
# Description: A script for turning dataset to numeric for  proper matching
#
# NOTE: Readme available for instructions to set up for RapidMiner
#
# NOTE: 'CONST_CLASS_LABEL' may need to change depending on your dataset "class column name"
#############################################################

import pandas as pd
import copy
import sys

columm_label_list = ["DNA", "RNA", "DRNA", "nonDRNA"]
file_path = sys.argv[1]

df = pd.read_csv(file_path)
CONST_CLASS_LABEL = "[Class]"

def extract_true_pos_tocsv(true_pos_class):
    new_df = copy.deepcopy(df)
    csv_file_name = "True_pos_" + true_pos_class + ".csv"
    for label in columm_label_list:
        if(label != true_pos_class):
            new_df[CONST_CLASS_LABEL].replace([label], ["No"], inplace=True)
    new_df[CONST_CLASS_LABEL].replace([true_pos_class], ["Yes"], inplace=True)
    new_df.to_csv(csv_file_name)

for column_val in columm_label_list:
    extract_true_pos_tocsv(column_val)
