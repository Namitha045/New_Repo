#############################################################################################################################
import csv
import sqlite3
from collections import namedtuple
from datetime import datetime
#############################################################################################################################

def str_to_date(text):
   return datetime.strptime(text, '%Y%m%d')
    
def temp_conv(text):
    if text:
        celcius = float(text) * 10
        return (celcius * 9/5) + 32
    return 0

Column = namedtuple('Column', 'src dest convert')
cols = [
    Column('DATE','day', str_to_date),
    Column('TMIN','min_temp', temp_conv),
    Column('TMAX', 'max_temp', temp_conv),
    Column('SNOW', 'snow', int)
]

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            record = []
            for col in cols:
                value = line[col.src]
                record.append(col.convert(value))
            yield record

#############################################################################################################################
if __name__=='__main__':
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS weather (
    day DATE,	    
    min_temp FLOAT, 
    max_temp FLOAT, 
    snow INTEGER)''')
    for r in read_csv('weather.csv'):
        cur.execute('INSERT INTO weather values (?,?,?,?)', r)
        conn.commit()
        print('Inserted rows:',cur.rowcount)
    conn.close()
    
