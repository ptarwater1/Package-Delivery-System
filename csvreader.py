"""
Patrick Tarwater #000919107
"""

import csv
from buildhashtable import HashMap

with open('inputs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    """
    First calls the class HashMap to create object of HashMap
    Followed by lists of truck one, truck two and the second trip of truck one
    """

    hash_table_insert = HashMap()
    truck_one = []
    truck_two = []
    truck_one_trip_two = []

    """
    CSV data is placed into key and value pairs that make up the nested dictionary inside the hash table
    O(N) Space-Time Complexity
    """

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
        status = 'At the Hub'
        iterate = [package_id, location_address, address, city, state, zipcode, deliver, weight, notes, start, status]
        key = package_id
        value = iterate

        """
        Creates the lists for each truck. Observes assumptions given by WGU as to what trucks can leave at what time
        as well as the packages that have deadlines. Other assumptions such as packages that must be linked and have
        addresses that must corrected are also considered. A nested list is created for each truck and values are added
        from the CSV into a hash table.        
        """

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
        hash_table_insert.insert(key, value)

    """
    Calls the hash map to obtain lists of each truck.
    O(1) Space-Time Complexity
    """

    def get_hash_map():
        return hash_table_insert

    """
    Obtains list of truck one.
    O(1) Space-Time Complexity
    """

    def check_truck_one_trip_one():
        return truck_one

    """
    Obtains list of truck two.
    O(1) Space-Time Complexity
    """

    def check_truck_two_trip_one():
        return truck_two

    """
    Obtains list of truck one's second trip.
    O(1) Space-Time Complexity
    """

    def check_truck_one_trip_two():
        return truck_one_trip_two

