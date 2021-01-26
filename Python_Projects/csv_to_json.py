#############################################################################################################################
import json
import csv
import bz2
from collections import namedtuple
from datetime import datetime
#############################################################################################################################

def parse_datetime(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')

def read_csv(filename):
    with bz2.open(filename, 'rt') as f:
        reader = csv.DictReader(f)
        for csv_record in reader:
            record = {}
            for col in columns:
                value = csv_record[col.src]
                record[col.dest] = col.convert(value)
            yield record

def encode_time(obj):
    if not isinstance(obj, datetime):
        return obj
    return obj.isoformat()

Column = namedtuple('Column', 'src dest convert')

columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_datetime),
    Column('tpep_pickup_datetime', 'pickup_time', parse_datetime),
    Column('trip_distance', 'distance', float),
]
  
with open('csv_into_json.json','w') as fp:
    for record in read_csv('taxi.csv.bz2'):
        data = json.dumps(record, default=encode_time)
        fp.write(f'{data}\n')
        


        
        



        