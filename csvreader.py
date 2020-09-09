import csv
from buildhashtable import HashMap

with open('inputs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    hash_table_insert = HashMap()  # creates object hashMap
    truck_one = []  # list of truck one
    truck_two = []  # list of truck two
    truck_one_trip_two = []  # second trip of truck one

