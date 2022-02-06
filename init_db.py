import sqlite3 

query_string =  """CREATE TABLE sents
                (
                    sent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sentlike VARCHAR(10),
                    pdf_name CHAR(50),
                    page_nr INT,
                    korrekt_annotering CHAR(50),
                    hvem_annoterede CHAR(50),
                    udtræk VARCHAR(10),
                    hvem_verificerede CHAR(50),
                    verifikation CHAR(50)
                );"""

query_string =  """CREATE TABLE annotations
                (
                    sent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sentlike VARCHAR(10),
                    pdf_name CHAR(50),
                    page_nr INT,
                    korrekt_annotering CHAR(50),
                    hvem_annoterede CHAR(50),
                    udtræk VARCHAR(10),
                    hvem_verificerede CHAR(50),
                    verifikation CHAR(50),
                    regex_annotering INT
                );"""



conn = sqlite3.connect('test.db')
conn.execute(query_string)

def add_annotation(values):
        
    conn.execute(f"""
        INSERT INTO annotations (sentlike, pdf_name, page_nr, regex_annotering)
        VALUES (?, "eksempel.pdf", 0, 2)
    """, values)
    conn.commit()


with open("test_data.csv", "r") as f:
    for s in f.readlines():
        add_annotation([s.strip("\n")])
