import pandas as pd
import numpy as np
import sys

file_appending_from = sys.argv[1]
columns_to_extract = sys.argv[2]
file_to_append_to = sys.argv[3]
CONST_CLASS_LABEL = "Class"
dataset = pd.read_csv(file_appending_from)

if "new" in file_to_append_to:
    df = pd.DataFrame()
else:
    df = pd.read_csv(file_to_append_to)
    del df[CONST_CLASS_LABEL]

if columns_to_extract == "all":
    columns = dataset.columns
else:
    columns_to_extract = pd.read_csv(columns_to_extract)
    columns = columns_to_extract['Column'].values
    
for column in columns:
    df = pd.concat([df, dataset[[column]]], axis=1)
df = pd.concat([df, dataset[[CONST_CLASS_LABEL]]], axis=1)
df.to_csv(file_to_append_to, index=False)
