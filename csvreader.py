import csv
from buildhashtable import HashMap

with open('inputs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    hash_table_insert = HashMap()  # Calls the Hashmap class to create an object of Hashmap
    truck_one = []  # list of truck one
    truck_two = [] # list that represents the second truck delivery
    truck_one_trip_two = [] # list that represents the final truck delivery

    # Read in values from CSV file and insert them into key / value pairs
    # these values are what makes up the nested dictionary inside of the Hash table
    # Space-time complexity is O(N)
    for row in readCSV:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deliver = row[5]
        weight = row[6]
        notes = row[7]
        start = ''
        location_address = ''
        status = 'At Hub'
        iterate = [package_id, location_address, address, city, state, zipcode, deliver, weight, notes, start, status]
        key = package_id
        value = iterate
        # In place constraints to create a list of packages that are loaded onto the trucks
        # The data structure here focuses on moving all attributes of a package into a nested listed.
        # This allows for quick lookup and sorting that can be based on every package detail
        # Below is the set of constraints that determine which packages are loaded in either of the two trucks
        if '9:00 AM' in value[6] or '10:30 AM' in value[6]:
            truck_one.append(value)
        if 'Delayed' in value[8]:
            truck_two.append(value)
        if '5383 South' in value[2]:
            truck_one.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            truck_one_trip_two.append(value)
        if value not in truck_one and value not in truck_two and value not in truck_one_trip_two:
            if len(truck_two) > len(truck_one_trip_two):
                truck_one_trip_two.append(value)
            else:
                truck_two.append(value)
        hash_table_insert.insert(key, value)  # adds all values in csv file to a hash table

    # function used to get the full list of values at start of day
    # Space-time complexity is O(1)
    def get_hash_map():
        return hash_table_insert

    # function used to grab the packages that are loaded into the first truck
    # Space-time complexity is O(1)
    def check_truck_one_trip_one():
        return truck_one

    # function used to grab the packages that are loaded into the second truck
    # Space-time complexity is O(1)
    def check_truck_two_trip_one():
        return truck_two

    # function used to grab the packages that are loaded into the first truck last
    # Space-time complexity is O(1)
    def check_truck_one_trip_two():
        return truck_one_trip_two

