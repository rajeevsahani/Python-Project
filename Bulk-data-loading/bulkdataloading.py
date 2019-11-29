import csv
import sqlite3 as sql
import sys
db='record.db'
query="""insert or ignore into tasks(id,name,age) values (:id,:name,:age) """
with open("tasks.csv","rt") as f:
    csv_reader=csv.DictReader(f)
    with sql.connect(db) as conn:
        cur=conn.cursor()
        cur.executemany(query,csv_reader);
print("data uploaded in database successfully.")
