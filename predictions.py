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
