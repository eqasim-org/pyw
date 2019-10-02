import data
import pandas as pd
import numpy as np

def ipf(df, marginals, weight = "weight", initial_weight = None, iterations = 100):
    weights = df[initial_weight].values if not initial_weight is None else np.ones((len(df),))

    masks = []
    targets = []

    for marginal in marginals:
        for index, values in marginal.iterrows():
            marginal_mask = np.ones((len(df),), dtype = np.bool)
            columns = list(marginal.columns)

            for column_index, column in enumerate(columns):
                if not column == weight:
                    marginal_mask &= df[column] == values[column_index]

            masks.append(marginal_mask)
            targets.append(values[columns.index(weight)])

    for i in range(iterations):
        for mask, target in zip(masks, targets):
            total = np.sum(weights[mask])
            weights[mask] *= target / total

    return weights
