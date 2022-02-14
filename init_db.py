import sqlite3 
import pandas as pd

# query_string =  """CREATE TABLE sents
#                 (
#                     paragraph_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     paragraph_text VARCHAR(10),
#                     doc_id CHAR(50),
#                     paragraph_number INT,
#                     korrekt_annotering CHAR(50),
#                     hvem_annoterede CHAR(50),
#                     udtræk VARCHAR(10),
#                     hvem_verificerede CHAR(50),
#                     verifikation CHAR(50)
#                 );"""

# "paragraph_id INTEGER PRIMARY KEY AUTOINCREMENT"



con = sqlite3.connect('test.db')
df_short = pd.read_csv("UN_annotation_short_version.csv")
df_short["paragraph_id"] = df_short.index
df_short["aktive_learning_annotation"] = 2
df_short.to_sql(name = "annotations", con = con)
columns_to_add = ["korrekt_annotering CHAR(50)",
                    "hvem_annoterede CHAR(50)",
                    "udtræk VARCHAR(10)",
                    "hvem_verificerede CHAR(50)",
                    "verifikation CHAR(50)"]
add_col = lambda col:  con.execute(f"ALTER TABLE annotations ADD {col}")
for i in columns_to_add: 
    add_col(i)
