import pandas as pd

def marginals(df, columns, values = {}, weight = "weight"):
    marginals = []

    for marginal_columns in columns:
        marginal_columns = list(marginal_columns)

        if len(marginal_columns) > 1:
            index = pd.MultiIndex.from_product(
                iterables = (
                    df[column].unique() if not column in values else values[column]
                    for column in marginal_columns
                ),
                names = marginal_columns
            )
        else:
            index_column = marginal_columns[0]

            index = pd.Index(
                df[index_column].unique() if not index_column in values else values[index_column],
                name = index_column
            )

        marginals.append(df[
            marginal_columns + [weight]
        ].groupby(marginal_columns).sum().reindex(index).fillna(0.0).reset_index())

    return marginals
