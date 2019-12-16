# Pre-Processing Scripts

## Smote/Tomek
    
    Info: 
        1.smote_tomek_rmp.py can be plugged into RapidMiner
        2.smote_tomek.py can be run outside of RapidMiner to produce csv
        NOTE: You may need to change the constant in the scripts that defines the name of the class label.

    How to run smote_tomek_rmp.py in RapidMiner:
        1. Install Python Scripting Extension in RapidMiner
            a. Extensions -> Marketplace -> Seach for Python Scripting
        2. Install anacondas (dependency for RapidMiner Python Scripting)
        3. Set up python env for RapidMiner
            a. Preferences -> Select Python Scripting tab
            b. Add the installation directory of your conda installation
        4. Add Execute Python Operator in appropriate place in RapidMiner
            ** For cross validation it should go inside of cross validation before training model is used.
        5. Specify the path for the script file in Execute Python Operator.
        6. Pip install imblearn, pandas numpy and ccv
        7. numeric_dataframe.py should be used as operator before being plugged into cross validation so that testing and training data are the same. 
        
        
    How to run smote_tomek.py:
        1. Pip install imblearn, pandas, numpy
        2. Execute passing in:
            a. name/path of file to smote
            b. name of desired csv file
        e.g. python smote_tomek.py fileToSmote.csv resultFile.csv


## TwoClassDataFrame 
    Info:
        1. two_class_dataframe_rmp.py can be plugged into RapidMiner
            a. This will only produce ONE true positive class label and you will have to update which one you want to be positive.
        2. two_class_dataframe.py is to be run outside of RapidMiner
            a. This will Produce all four class labels as true positive (4 total csv)
        
    How to run two_class_dataframe.py:
        1. Pip install pandas
        2. Execute passing in:
            a. name/path of file to extract true positives from
        *** 4 new csvs will be produced in the pwd.
        
        
