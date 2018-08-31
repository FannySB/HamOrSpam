#! /usr/bin/env python3
import argparse
import os
import csv
import sys

from bayes import Classifier
from bayes import Training


def load_dataset(dataset_path):
    with open(dataset_path, 'r') as dataset_file:
        reader = csv.reader(dataset_file)
        dataset = [(com, label) for label, com, one, second, third in reader]
        return dataset

def test_classifier_accuracy(classifier, dataset_path):
    n_data, n_positives = 0, 0
    
    DATASET = load_dataset(TESTDATA_PATH)
    for (communication, label) in DATASET:
        n_data += 1
        try:
            predicted_label = classifier.classify(communication)
            if predicted_label == label:
                n_positives += 1
        except:
            continue

    return n_positives / n_data
    

TESTDATA_PATH = 'test.csv'
TRAINDATA_PATH = 'train.csv'
LABELS = ['ham', 'spam']
classifier = Classifier(LABELS)

print('BAYES')
training = Training(LABELS, TRAINDATA_PATH)
training.train()
accuracy = test_classifier_accuracy(classifier, TESTDATA_PATH)
print('Accuracy: %f' % accuracy)

