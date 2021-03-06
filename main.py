#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import numpy

# Data Visualization
import titanic_visualizations
from IPython.display import display
from accuracy import accuracy_score
from predictions import predictions_no_features, predictions_one_feature, predictions_two_features, predictions_multi_features

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pandas.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
# display(full_data.head())

# Store the survived feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis=1)

# Show the new dataset with Survived removed
# display(data.head())

# Test the accuracy score against our predictions
predictions = pandas.Series(numpy.ones(5, dtype=int))
print(accuracy_score(outcomes[:5], predictions))

predictions = predictions_no_features(data)
print(accuracy_score(outcomes, predictions))

predictions = predictions_one_feature(data)
print(accuracy_score(outcomes, predictions))

predictions = predictions_two_features(data)
print(accuracy_score(outcomes, predictions))

predictions = predictions_multi_features(data)
print(accuracy_score(outcomes, predictions))
