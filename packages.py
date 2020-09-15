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

route_one = []
route_two = []
route_three = []
distance_route_one = []
distance_route_two = []
distance_route_three = []
# the times below represent the times that each truck leaves the hub
departure_route_one = '08:00:00'
departure_route_two = '09:05:00'
departure_route_three = '11:00:00'

# the operations below convert the string time into a datetime.timedelta
(h, m, s) = departure_route_one.split(':')
convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = departure_route_two.split(':')
convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = departure_route_three.split(':')
convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# for loop updates the delivery status of all packages in truck 1 to when the truck leaves the station
i = 0  # counter to iterate through for loop
# Space-time complexity is O(N)
for value in check_truck_one_trip_one():
    check_truck_one_trip_one()[i][9] = departure_route_one
    route_one.append(check_truck_one_trip_one()[i])
    i += 1
# this for loop compares the addresses on truck one to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    first_variable_count = 0
    for k in route_one:
        for j in distances.address_check():
            if k[2] == j[2]:
                distance_route_one.append(j[0])
                route_one[first_variable_count][1] = j[0]
        first_variable_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
find_shortest_path(route_one, 1, 0)
truck_one_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
initial_package = 0
for index in range(len(optimal_index_truck_one())):
    try:
        # calculate the total distance of the truck
        truck_one_distance = distance_inspection(int(optimal_index_truck_one()[index]), int(optimal_index_truck_one()[index + 1]), truck_one_distance)
        # calculate the distance of each package along the route
        deliver_package = time_status_truck_one(check_current_distance(int(optimal_index_truck_one()[index]), int(optimal_index_truck_one()[index + 1])))
        optimal_list_truck_one()[initial_package][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_one()[initial_package][0]), route_one)
        initial_package += 1
    except IndexError:
        pass
# for loop updates the delivery status of all packages in truck 2 to when they leave the station
i = 0  # counter to iterate through for loop
# Space-time complexity is O(N)
for value in check_truck_two_trip_one():
    check_truck_two_trip_one()[i][9] = departure_route_two
    route_two.append(check_truck_two_trip_one()[i])
    i += 1
# this for loop compares the addresses on truck two to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    secondary_package = 0
    for k in route_two:
        for j in distances.address_check():
            if k[2] == j[2]:
                distance_route_two.append(j[0])
                route_two[secondary_package][1] = j[0]
        secondary_package += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
find_shortest_path(route_two, 2, 0)
truck_two_distance = 0
# this for loop takes the values in the second truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
initial_package_two = 0
for index in range(len(optimal_index_truck_two())):
    try:
        # calculate the total distance of the truck
        truck_two_distance = distance_inspection(int(optimal_index_truck_two()[index]), int(optimal_index_truck_two()[index + 1]), truck_two_distance)
        # calculate the distance of each package along the route
        deliver_package = time_status_truck_two(check_current_distance(int(optimal_index_truck_two()[index]), int(optimal_index_truck_two()[index + 1])))
        optimal_list_truck_two()[initial_package_two][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_two()[initial_package_two][0]), route_two)
        initial_package_two += 1
    except IndexError:
        pass

# for loop updates the delivery status of all packages in truck 1 (second delivery) to 'En route'
i = 0
# Space-time complexity is O(N)
for value in check_truck_one_trip_two():
    check_truck_one_trip_two()[i][9] = departure_route_three
    route_three.append(check_truck_one_trip_two()[i])
    i += 1
# this for loop compares the addresses on truck one (second delivery) to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    initial_package_three = 0
    for k in route_three:
        for j in distances.address_check():
            if k[2] == j[2]:
                distance_route_three.append(j[0])
                route_three[initial_package_three][1] = j[0]
        initial_package_three += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
find_shortest_path(route_three, 3, 0)
truck_three_distance = 0
# this for loop takes the values in the third truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
tertiary_package = 0
for index in range(len(optimal_index_truck_three())):
    try:
        # calculate the total distance of the truck
        truck_three_distance = distance_inspection(int(optimal_index_truck_three()[index]), int(optimal_index_truck_three()[index + 1]), truck_three_distance)
        # calculate the distance of each package along the route
        deliver_package = time_status_truck_three(check_current_distance(int(optimal_index_truck_three()[index]), int(optimal_index_truck_three()[index + 1])))
        optimal_list_truck_three()[tertiary_package][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_three()[tertiary_package][0]), route_three)
        tertiary_package += 1
    except IndexError:
        pass

# function returns total distance of all 3 trips to calculate the distance of all packages
# Space-time complexity is O(1)
def final_mileage():
    total_distance = truck_one_distance + truck_two_distance + truck_three_distance
    return total_distance

