

def calculate_marginals(df, columns, values = None, weight_column = "weight"):
    for marginal_columns in columns:
        marginal_columns = list(marginal_columns)
        df[marginal_columns + [weight_column]].groupby(marginal_columns)
