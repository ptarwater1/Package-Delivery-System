"""
Patrick Tarwater #000919107
"""

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

"""
The times determine departures of each delivery route from the hub.
"""

departure_route_one = '08:00:00'
departure_route_two = '09:05:00'
departure_route_three = '11:00:00'

"""
Convert strings into datetime using timedelta.
"""

(h, m, s) = departure_route_one.split(':')
convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = departure_route_two.split(':')
convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = departure_route_three.split(':')
convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

"""
A for loop updates the status of the delivery of every package in truck one to the time of departure.
i is the counter for each loop iteration.
O(N) Space-Time Complexity.
"""

i = 0

for value in check_truck_one_trip_one():
    check_truck_one_trip_one()[i][9] = departure_route_one
    route_one.append(check_truck_one_trip_one()[i])
    i += 1

    """
    For loop that compares the addresses on truck one to the list of addresses and adds the index to the list.
    O(N^2) Space-Time Complexity
    """

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

"""
The greedy algorithm is called to sort the packages.
"""

find_shortest_path(route_one, 1, 0)
truck_one_distance = 0

"""
For loop retrieves the truck one values and executes the values through the distance functions found in distances file.
O(N) Space-Time Complexity
"""

initial_package = 0
for index in range(len(optimal_index_truck_one())):
    try:

        """
        Total distance of truck one is determined.
        """

        truck_one_distance = distance_inspection(int(optimal_index_truck_one()[index]),
                                                 int(optimal_index_truck_one()[index + 1]), truck_one_distance)

        """
        Distance of each package en route is determined.
        """

        deliver_package = time_status_truck_one(check_current_distance(int(optimal_index_truck_one()[index]),
                                                                       int(optimal_index_truck_one()[index + 1])))
        optimal_list_truck_one()[initial_package][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_one()[initial_package][0]), route_one)
        initial_package += 1
    except IndexError:
        pass

"""
A for loop updates the status of the delivery of every package in truck two to the time of departure.
i is the counter for each loop iteration.
O(N) Space-Time Complexity.
"""

i = 0

for value in check_truck_two_trip_one():
    check_truck_two_trip_one()[i][9] = departure_route_two
    route_two.append(check_truck_two_trip_one()[i])
    i += 1

    """
    For loop that compares the addresses on truck two to the list of addresses and adds the index to the list.
    O(N^2) Space-Time Complexity
    """

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

"""
The greedy algorithm is called to sort the packages.
"""

find_shortest_path(route_two, 2, 0)
truck_two_distance = 0

"""
For loop retrieves the truck two values and executes the values through the distance functions found in distances file.
O(N) Space-Time Complexity
"""

initial_package_two = 0
for index in range(len(optimal_index_truck_two())):
    try:

        """
        Total distance of truck two is determined.
        """

        truck_two_distance = distance_inspection(int(optimal_index_truck_two()[index]),
                                                 int(optimal_index_truck_two()[index + 1]), truck_two_distance)

        """
        Distance of each package en route is determined.
        """

        deliver_package = time_status_truck_two(check_current_distance(int(optimal_index_truck_two()[index]),
                                                                       int(optimal_index_truck_two()[index + 1])))
        optimal_list_truck_two()[initial_package_two][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_two()[initial_package_two][0]), route_two)
        initial_package_two += 1
    except IndexError:
        pass


"""
For loop updates the status of delivery for all packages in trip two of truck one to "En route".
O(N) Space-Time Complexity
"""

i = 0

for value in check_truck_one_trip_two():
    check_truck_one_trip_two()[i][9] = departure_route_three
    route_three.append(check_truck_one_trip_two()[i])
    i += 1

"""
For loop checks the addresses of truck one trip two against the address list and appends the index of address
to the list.
O(N^2) Space-Time Complexity.
"""

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

"""
The greedy algorithm is called to sort the packages.
"""

find_shortest_path(route_three, 3, 0)
truck_three_distance = 0

"""
For loop retrieves truck three values and executes the values through the distance functions found in distances file.
O(N) Space-Time Complexity
"""

tertiary_package = 0
for index in range(len(optimal_index_truck_three())):
    try:

        """
        Total distance of the truck is determined.
        """
        truck_three_distance = distance_inspection(int(optimal_index_truck_three()[index]),
                                                   int(optimal_index_truck_three()[index + 1]), truck_three_distance)

        """
        Distance of each package en route is determined.
        """

        deliver_package = time_status_truck_three(check_current_distance(int(optimal_index_truck_three()[index]),
                                                                         int(optimal_index_truck_three()[index + 1])))
        optimal_list_truck_three()[tertiary_package][10] = (str(deliver_package))
        get_hash_map().update(int(optimal_list_truck_three()[tertiary_package][0]), route_three)
        tertiary_package += 1
    except IndexError:
        pass

"""
The final mileage of all the delivery routes given via the total_distance function.
O(1) Space-Time Complexity
"""


def final_mileage():
    total_distance = truck_one_distance + truck_two_distance + truck_three_distance
    return total_distance

