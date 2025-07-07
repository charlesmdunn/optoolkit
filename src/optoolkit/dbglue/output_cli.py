
import argparse
import csv
import sqlite3
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("-d", "--database", type=str, help="what?")
parser.add_argument("-t", "--table_name", help="what?")
parser.add_argument("-f", "--file_csv", type=argparse.FileType('r'), help="what?")
args=parser.parse_args()


def table_to_csv(db,table,csv_fp):

    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows=cur.fetchall()
    writer=csv.writer(csv_fp)
    writer.writerow([i[0] for i in cur.description])
    writer.writerows(rows) 
    cur.close()
    con.close()




def main():

#      tuple_to_table(args.database, args.table_name, args.file_csv) 
    table_to_csv(args.database, args.table_name, args.file_csv) 

    #tuple_to_table(Path("~/Databases/keymaps.db").expanduser(),"test_new",
                   #Path("~/GitHub/Keyboard/fapple2k/ref/zmk2.csv").expanduser())
if __name__ == "__main__":
    main()
