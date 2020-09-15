from csvreader import check_truck_one_trip_one
from csvreader import check_truck_one_trip_two
from csvreader import check_truck_two_trip_one
from distances import distance_inspection
from distances import time_status_truck_one
from distances import time_status_truck_two
from distances import time_status_truck_three
from distances import check_current_distance
from distances import find_shortest_path
from distances import optimal_index_truck_one
from distances import optimal_list_truck_one
from distances import optimal_index_truck_two
from distances import optimal_list_truck_two
from distances import optimal_index_truck_three
from distances import optimal_list_truck_three
from csvreader import get_hash_map

import datetime
import distances

first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distance_list = []
second_truck_distance_list = []
third_truck_distance_list = []
# the times below represent the times that each truck leaves the hub
first_time = '08:00:00'
second_time = '09:05:00'
third_time = '10:45:00'

# the operations below convert the string time into a datetime.timedelta
(h, m, s) = first_time.split(':')
convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = second_time.split(':')
convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = third_time.split(':')
convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# for loop updates the delivery status of all packages in truck 1 to when the truck leaves the station
i = 0  # counter to iterate through for loop
# Space-time complexity is O(N)
for value in check_truck_one_trip_one():
    check_truck_one_trip_one()[i][9] = first_time
    first_delivery.append(check_truck_one_trip_one()[i])
    i += 1
# this for loop compares the addresses on truck one to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    first_variable_count = 0
    for k in first_delivery:
        for j in distances.address_check():
            if k[2] == j[2]:
                first_truck_distance_list.append(j[0])
                first_delivery[first_variable_count][1] = j[0]
        first_variable_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
find_shortest_path(first_delivery, 1, 0)
first_truck_total_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
first_truck_package_id = 0
for index in range(len(optimal_index_truck_one())):
    try:
        # calculate the total distance of the truck
        first_truck_total_distance = distance_inspection(int(optimal_index_truck_one()[index]), int(optimal_index_truck_one()[index + 1]), first_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = time_status_truck_one(check_current_distance(int(optimal_index_truck_one()[index]), int(optimal_index_truck_one()[index + 1])))
        optimal_list_truck_one()[first_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_one()[first_truck_package_id][0]), first_delivery)
        first_truck_package_id += 1
    except IndexError:
        pass
# for loop updates the delivery status of all packages in truck 2 to when they leave the station
i = 0  # counter to iterate through for loop
# Space-time complexity is O(N)
for value in check_truck_two_trip_one():
    check_truck_two_trip_one()[i][9] = second_time
    second_delivery.append(check_truck_two_trip_one()[i])
    i += 1
# this for loop compares the addresses on truck two to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    second_variable_count = 0
    for k in second_delivery:
        for j in distances.address_check():
            if k[2] == j[2]:
                second_truck_distance_list.append(j[0])
                second_delivery[second_variable_count][1] = j[0]
        second_variable_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
find_shortest_path(second_delivery, 2, 0)
second_truck_total_distance = 0
# this for loop takes the values in the second truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
second_truck_package_id = 0
for index in range(len(optimal_index_truck_two())):
    try:
        # calculate the total distance of the truck
        second_truck_total_distance = distance_inspection(int(optimal_index_truck_two()[index]), int(optimal_index_truck_two()[index + 1]), second_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = time_status_truck_two(check_current_distance(int(optimal_index_truck_two()[index]), int(optimal_index_truck_two()[index + 1])))
        optimal_list_truck_two()[second_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_two()[second_truck_package_id][0]), second_delivery)
        second_truck_package_id += 1
    except IndexError:
        pass

# for loop updates the delivery status of all packages in truck 1 (second delivery) to 'En route'
i = 0
# Space-time complexity is O(N)
for value in check_truck_one_trip_two():
    check_truck_one_trip_two()[i][9] = third_time
    third_delivery.append(check_truck_one_trip_two()[i])
    i += 1
# this for loop compares the addresses on truck one (second delivery) to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    third_variable_count = 0
    for k in third_delivery:
        for j in distances.address_check():
            if k[2] == j[2]:
                third_truck_distance_list.append(j[0])
                third_delivery[third_variable_count][1] = j[0]
        third_variable_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
find_shortest_path(third_delivery, 3, 0)
third_truck_total_distance = 0
# this for loop takes the values in the third truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
third_truck_package_id = 0
for index in range(len(optimal_index_truck_three())):
    try:
        # calculate the total distance of the truck
        third_truck_total_distance = distance_inspection(int(optimal_index_truck_three()[index]), int(optimal_index_truck_three()[index + 1]), third_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = time_status_truck_three(check_current_distance(int(optimal_index_truck_three()[index]), int(optimal_index_truck_three()[index + 1])))
        optimal_list_truck_three()[third_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_three()[third_truck_package_id][0]), third_delivery)
        third_truck_package_id += 1
    except IndexError:
        pass

# function returns total distance of all 3 trips to calculate the distance of all packages
# Space-time complexity is O(1)
def total_distance():
    total_distance = first_truck_total_distance + second_truck_total_distance + third_truck_total_distance
    return total_distance

