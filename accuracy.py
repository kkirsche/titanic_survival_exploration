#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def accuracy_score(truth, prediction):
    """Returns the accuracy score for input truth and prediction."""

    # Ensure that the number of predictions match the number of outcomes
    if len(truth) == len(prediction):
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format(
            (truth == prediction).mean() * 100
        )
    else:
        return "Number of predictions does not match number of outcomes!"
