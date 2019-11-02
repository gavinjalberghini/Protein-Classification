######
# Author: Gavin Alberghini
# Date: 10/21/2019
# Description: A script used to understand measured outcomes of our predictions
######
import math

dna_class = bin(0)
rna_class = bin(1)
both_class = bin(2)
neither_class = bin(3)
num_labels = 4


# Build the full confusion matrix from the prediction vs actual results
def generate_confusion(prediction, actual):
    confusion = [[0] * num_labels for i in range(0, num_labels)]

    for counter in range(0, len(actual)):
        x_index = int(prediction[counter], 2)
        y_index = int(actual[counter], 2)
        confusion[x_index][y_index] = confusion[x_index][y_index] + 1

    return confusion


# ITEMS TO CONSIDER:
# - Total number of samples in one class are equal to the sum of a row
# - Total TP's rest on the diagonal of the matrix
# - Total FN's for a class is the sum of the row minus TP
# - Total FP's for a class is the sum of the column minus TP
# - Total TN's for a class is the sum of the table minus the class column and row
def breakdown_confusion(confusion):

    reduced_confusion_results = []
    row_sums = list(map(sum, confusion))
    col_sums = [sum(col) for col in zip(*confusion)]

    for x in range(0, num_labels):
        tp = confusion[x][x]
        fp = col_sums[x] - tp
        fn = row_sums[x] - tp
        tn = sum(col_sums) + sum(row_sums) - col_sums[x] - row_sums[x]
        label_result = [tp, tn, fp, fn]
        reduced_confusion_results.append(label_result)

    return reduced_confusion_results


# Perform detailed scoring calculations
def generate_statistics(confusion):
    sens = 100 * confusion[0] / (confusion[0] + confusion[3])
    spec = 100 * confusion[1] / (confusion[1] + confusion[2])
    predict_acc = 100 * (confusion[0] + confusion[1]) / (sum(confusion))
    mcc = (confusion[0] * confusion[1] - confusion[2] * confusion[3]) / math.sqrt((confusion[0] + confusion[2])
                                                                                  * (confusion[0] + confusion[3])
                                                                                  * (confusion[1] + confusion[2])
                                                                                  * (confusion[1] + confusion[3]))

    stats = (sens, spec, predict_acc, mcc)
    return stats


# Perform overall scoring of results and return the output
def generate_metrics(prediction, actual):
    confusion = generate_confusion(prediction, actual)

    reduced_confusions = breakdown_confusion(confusion)
    dna_confusion = reduced_confusions[0]
    rna_confusion = reduced_confusions[1]
    both_confusion = reduced_confusions[2]
    neither_confusion = reduced_confusions[3]

    dna_stats = generate_statistics(dna_confusion)
    rna_stats = generate_statistics(rna_confusion)
    both_stats = generate_statistics(both_confusion)
    neither_stats = generate_statistics(neither_confusion)

    avg_mcc = (dna_stats[3] + rna_stats[3] + both_stats[3] + neither_stats[3]) / 4
    acc = 100 * (dna_confusion[0] + rna_confusion[0] + both_confusion[0] + neither_stats[0]) / len(actual)


    metrics = [dna_stats, rna_stats, both_stats, neither_stats, avg_mcc, acc]

    return metrics

