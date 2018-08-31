# coding=utf-8
import csv
import sys
import re
import numpy as np
import math

class Classifier:
    """Basic Naïve Bayes classifier."""

    def __init__(self, label_array):
        """label_array : array of possible classification."""
        self.label_array = label_array
        self.n_classes = len(label_array)


    def classify(self, communication):
        class_prob = {}
        for label in self.label_array:
            class_prob[label] = 1

        for word in getWords(communication):
            if word in dict_label_prob:
                for label in self.label_array:
                    class_prob[label] *= dict_label_prob[word][label]
        likelihood = 0
        best_class = '';
        for label in class_prob:
            if likelihood < class_prob[label]:
                likelihood = class_prob[label]
                best_class = label
        
        return best_class


class Training:
    """Basic Naïve Bayes Training."""

    def __init__(self, label_array, TRAINDATA_PATH):
        """label_array : array of possible classification."""
        self.label_array = label_array
        self.n_classes = len(label_array)
        self.DATASET_PATH = TRAINDATA_PATH


    def load_dataset(self, dataset_path):
        with open(dataset_path, 'r') as dataset_file:
            reader = csv.reader(dataset_file)
            dataset = [(com, label) for label, com, one, second, third in reader]
            return dataset


    def train(self):
        DATASET = self.load_dataset(self.DATASET_PATH)
        labels_words_count = {} #list of all word per labels

        labels_stats = {} 
        for label in self.label_array:
                labels_words_count[label] = {}
                labels_stats[label] = 0

        vocabulary = {}
        nb_communications = 0

        for communication, label in DATASET:
            nb_communications += 1
            if label not in labels_words_count:
                labels_words_count[label] = {}
                print('ERROR: label %s not in the list' % label)
                labels_stats[label] = 0

            labels_stats[label] += 1

            for word in getWords(communication):
                # add to dictionary
                if word not in vocabulary:
                    vocabulary[word] = 1
                else:
                    vocabulary[word] += 1

                # add to label's dictionary
                if word not in labels_words_count[label]:
                    labels_words_count[label][word] = 1
                else:
                    labels_words_count[label][word] += 1

        for word, count in vocabulary.items():
            dict_label_prob[word] = {}
            for label in self.label_array:
                if word not in labels_words_count[label]:
                    dict_label_prob[word][label] = 0
                else:
                    prob = labels_words_count[label][word] / count * (labels_stats[label] / nb_communications)
                    dict_label_prob[word][label] = prob


dict_label_prob = {}

def getWords(communication):
    words = []
    for w in communication.split():
        w = w.lower()
        match = re.search('[a-z]{3,}', w)
        if match:
            words.append(w)
    return words