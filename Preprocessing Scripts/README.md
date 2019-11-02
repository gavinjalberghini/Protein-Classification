# Pre-Processing Scripts

# Smote/Tomek
    
    Info: 
        1.SmoteTomek.py can be plugged into RapidMiner
        2.SmoteTomekNonRapidMiner.py can be run outside of RapidMiner to produce csv
        NOTE: You may need to change the constant in the scripts that defines the name of the class label.
        
    How to run SmoteTomek.py in RapidMiner:
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
        
        
    How to run SmoteTomekNonRapidMiner.py:
        1. Pip install imblearn, pandas, numpy
        2. Execute passing in:
            a. name/path of file to smote
            b. name of desired csv file
        e.g. python SmoteTomekNonRapidMiner.py fileToSmote.csv resultFile.csv

        
        
