import argparse
import csv
import sqlite3
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("-d", "--database", type=str, help="what?")
parser.add_argument("-t", "--table_name", help="what?")
parser.add_argument("-f", "--file_csv", type=argparse.FileType('r'), help="what?")
args=parser.parse_args()


#def table_to_csv(db,table,csv_fp):

    
def tuple_to_table(db,table, csv_fp): 

    data_tuple=[]
#    with open(csv_fp,newline='') as csvfile:
#        reader =csv.DictReader(csvfile)
#        data_tuple=tuple(reader)

    reader =csv.DictReader(csv_fp)
    data_tuple=tuple(reader)

    header_dict={} 
    for key in data_tuple[0].keys():
        header_dict.update({key: "TEXT"})
    print(header_dict.items())
    con = sqlite3.connect(db)
    cur = con.cursor()
    create_header_str=""
    for key, value in header_dict.items():
        create_header_str=create_header_str+f"{key} {value}, "   
    create_header_str=create_header_str[:-2]
    print(create_header_str)
    
    insert_header_str=""
    for key in header_dict.keys():
        insert_header_str=insert_header_str+f":{key}, "
    insert_header_str=insert_header_str[:-2]
    print(insert_header_str)
    cur.execute(f"DROP TABLE IF EXISTS {table}")
    cur.execute(f"CREATE TABLE {table}({create_header_str})")
    cur.executemany(f"INSERT INTO {table} VALUES({insert_header_str})",data_tuple)
    con.commit()
    cur.close()
    con.close()

def main():

    tuple_to_table(args.database, args.table_name, args.file_csv) 
#        table_to_csv(args.database, args.table_name, args.file_csv) 

    #tuple_to_table(Path("~/Databases/keymaps.db").expanduser(),"test_new",
                   #Path("~/GitHub/Keyboard/fapple2k/ref/zmk2.csv").expanduser())
if __name__ == "__main__":
    main()
