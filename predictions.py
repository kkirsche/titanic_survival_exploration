#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import titanic_visualizations


def predictions_no_features(data):
    """Model with no features. Always predicts a passenger did not survive."""

    predictions = []
    for _, passenger in data.iterrows():
        # Predict the survival of 'passenger'
        # We append 0, or died, because it is more likely that they died than
        # they survived, thus, this is the most probable outcome
        predictions.append(0)

    # Return our prediction
    return pandas.Series(predictions)


def predictions_one_feature(data):
    """Model with one feature:
           - Predict a passenger survived if they are female."""

    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)
    return predictions


def predictions_two_features(data):
    """Model with one feature:
           - Predict a passenger survived if they are female.
           - Predict a passenger survived if they are male and younger than 10 years old."""

    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            # Passenger is a male
            if passenger['Age'] < 10:
                predictions.append(1)
            else:
                predictions.append(0)
    return predictions


def predictions_multi_features(data):
    """Model with one feature:
           - Predict a passenger survived if they are female.
           - Predict a passenger survived if they are male and younger than 10 years old.
           - Predict a passenger survived if they were a first class or second class child"""

    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            if passenger['Pclass'] > 2:
                predictions.append(0)
            else:
                predictions.append(1)
        else:
            # Passenger is a male
            if passenger['Pclass'] == 3 or passenger['Parch'] == 0:
                predictions.append(0)
                continue

            if passenger['Age'] < 10:
                predictions.append(1)
            else:
                if passenger['Fare'] > 300:
                    predictions.append(1)
                else:
                    predictions.append(0)
    return predictions
