import pandas as pd
import numpy as np
import data, ipf

df = pd.read_csv("entd/Q_individu.csv", sep = ";", encoding = "latin1")

df = df[["SEXE", "AGE"]]

df["sex"] = df["SEXE"].apply(lambda x: "male" if x == 1 else "female").astype("category")
df["age_class"] = np.digitize(df["AGE"], [6, 18, 24, 40, 65])

df["weight"] = np.random.random((len(df),)) * 0.9 + 0.1

marginals = data.marginals(df, [["sex", "age_class"]])

ipf.ipf(df, marginals)

#print(marginals)
