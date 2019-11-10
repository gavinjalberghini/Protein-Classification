#

#

#





#
# Protein Classification Project

Submitted by:
Michael Fitzgerald, Jacob Unterman, Michael Poblacion, Gavin Alberghini













1. **1)****Description of the design for our predictive models**
  1. **a)****Pre-Processing Methods**

    1. **i)****CharCount Method**

We preprocessed the data into a count of the number of occurrences for each amino acid in each sequence.

    2. **ii)****SubString Matching**

    3. **iii)****N-grams Method**

    4. **iv)****PROFEAT Method**


  2. **b)****Model Selections**
    1. **i)****kNN**
    2. **ii)****SVM**
    3. **iii)****Neural Net**
    4. **iv)****Random Forest**
    5. **v)****CHAID**
Parameters used:
    6. **vi)****Decision Tree**
Parameters used:
      1. **(1)**Criterion: Gain Ratio
      2. **(2)**Maximal Depth: 20
      3. **(3)**Pruning: Yes
      4. **(4)**Confidence: 0.2
      5. **(5)**Pre Pruning: No

  3. **c)****Design Selections**
    1. **i)****Design 1**
    2. **ii)****Design 2**
    3. **iii)****Design 3**
    4. **iv)****Best Design**

2. **2)****Results of predictive models**

| Outcome | Quality Measure | Baseline Result | Design 1 | Design 2 | Design 3 | Best Design |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
| DNA | Sensitivity | 6.9 | 18.84 |   |   |   |
|   | Specificity | 99.3 | 97.84 |   |   |   |
|   | Predictive ACC | 95.2 | 97.53 |   |   |   |
|   | MCC | 0.132 | 0.07 |   |   |   |
|   |   |   |   |   |   |   |
| RNA | Sensitivity | 39.6 | 44.9 |   |   |   |
|   | Specificity | 98.9 | 97.6 |   |   |   |
|   | Predictive ACC | 95.3 | 96.86 |   |   |   |
|   | MCC | 0.501 | 0.29 |   |   |   |
|   |   |   |   |   |   |   |
| DRNA | Sensitivity | 4.5 | 28.57 |   |   |   |
|   | Specificity | 100 | 99.88 |   |   |   |
|   | Predictive ACC | 99.7 | 99.86 |   |   |   |
|   | MCC | 0.122 | 0.16 |   |   |   |
|   |   |   |   |   |   |   |
| nonDRNA | Sensitivity | 98.6 | 90.91 |   |   |   |
|   | Specificity | 29.8 | 89.02 |   |   |   |
|   | Predictive ACC | 91.3 | 90.64 |   |   |   |
|   | MCC | 0.428 | 0.69 |   |   |   |
|   |   |   |   |   |   |   |
| Average MCC |   | 0.265 | 0.3 |   |   |   |
| Accuracy |   | 90.8 | 89.02 |   |   |   |

1. **3)****Conclusions**
