import pandas as pd
import numpy as np
import sqlite3

df = pd.read_csv("UN_annotation_data.csv")
df_short = df.iloc[:100000,].drop("Unnamed: 0", axis=1)
#df_short.to_csv("UN_annotation_short_version.csv")

df = pd.read_csv("UN_annotation_data_short.csv")
df_short.to_sql(
    name = "annotations",
    con = sqlite3.connect('test.db'),
    )


