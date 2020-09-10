import csv
from buildhashtable import HashMap

with open('inputs.csv') as csvInputs:
    inputs_csv = csv.reader(csvInputs, delimiter=',')

    hash_table_insert = HashMap()  # creates object hashMap
    truck_one = []  # list of truck one
    truck_two = []  # list of truck two
    truck_one_trip_two = []  # second trip of truck one

    # values from CSV are inserted as key value pairs
    # Space time complexity is O(N)
    for row in inputs_csv:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deliver = row[5]
        weight = row[6]
        notes = row[7]
        start = ''
        location = ''
        status = ''
        iterate = [package_id, address, city, state, zip_code, deliver, weight, notes, start, location, status]
        key = package_id
        value = iterate
        # add comments
        if package_id == 9:
            address = '410 S State St'
            zip_code = '84111'
        if deliver != 'EOD':
            if 'None' or 'with' in value[8]:
                truck_one.append(value)
        if 'truck 2' in value[8]:
            truck_two.append(value)
        if 'Delayed' in value[8]:
            truck_two.append(value)
        if value not in truck_one and value not in truck_two and value not in truck_one_trip_two:
            if len(truck_two) > len(truck_one_trip_two):
                truck_one_trip_two.append(value)
            else:
                truck_two.append(value)
        hash_table_insert.insert(key, value)

    def check_truck_one_trip_one():
        return truck_one

    def check_truck_two_trip_one():
        return truck_two

    def check_truck_one_trip_two():
        return truck_one_trip_two

    def get_hash_map():
        return hash_table_insert

