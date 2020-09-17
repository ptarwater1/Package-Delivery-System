"""
Patrick Tarwater #000919107
"""

import csv
import datetime

"""
CSV file that contains the names of address of all of the delivery locations is read.
"""
with open('addresses.csv') as csv_name_file:
    csv_addresses = csv.reader(csv_name_file, delimiter=',')
    csv_addresses = list(csv_addresses)
"""
CSV file that contains the distance map between delivery locations is read.
"""

with open('distances.csv') as csvfile:
    csv_distances = csv.reader(csvfile, delimiter=',')
    csv_distances = list(csv_distances)

    """
    Inspects and iterates the distance between locations and returns the total distance.
    O(1) Space-Time Complexity
    """

    def distance_inspection(row_value, column_value, distance_sum):
        distance = csv_distances[row_value][column_value]
        if distance == '':
            distance = csv_distances[column_value][row_value]

        distance_sum += float(distance)
        return distance_sum

    """
    Inspects and iterates the current distance between locations and returns the current distance.
    O(1) Space-Time Complexity
    """

    def check_current_distance(row_value, column_value):
        distance = csv_distances[row_value][column_value]
        if distance == '':
            distance = csv_distances[column_value][row_value]
        return float(distance)

    """
    Declares the time for truck one departure.
    """

    first_time_list = ['8:00:00']
    second_time_list = ['9:05:00']
    third_time_list = ['11:00:00']

    """
    Trucks travel at 18 mph. Divmod is used to display a time an concats 00. This creates a string that is a timestamp
    that is split and transformed into a datetime using timedelta. This object is added to a sum that represents the
    total distance for a specified truck.
    O(N) runtime.
    """

    def time_status_truck_one(distance):
        mph = 18
        new_time = distance / mph
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        first_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in first_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    """
    Above function is repeated for truck two.
    """

    def time_status_truck_two(distance):
        mph = 18
        new_time = distance / mph
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        second_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in second_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    """
    Above function is repeated for truck three.
    """

    def time_status_truck_three(distance):
        mph = 18
        new_time = distance / mph
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        third_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in third_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    """
    Returns the objects regarding time that are used in the packages file.
    O(1) Space-Time Complexity
    """
    def address_check():
        return csv_addresses

    """
    Defines lists that represent the sorted trucks and are put in efficient order.
    """

    efficient_truck_one = []
    index_list_truck_one = []
    efficient_truck_two = []
    index_list_truck_two = []
    efficient_truck_three = []
    index_list_truck_three = []

    """
    A greedy algorithm is used to optimize the route for each truck. Three parameters are used; the list for each truck, 
    the number of the truck, the current location. 
    
    A base case of the algorithm is established in the first 'if' statement and end the recursion function once the
    input list reaches size 0. 
        
    The algorithm begins by using a "smallest value" of 25.0 which is used to compare every possible distance between 
    points that are available and checks if it is a smaller value. If a distance is less than the lowest value then it 
    is updated and the search goes on. 
    
    Once all distances and route possibilities are examined, the truck is ready for departure with the package list    
    provided and then adds that package objects and linked index to new lists. 
    
    The second parameter is checked and makes sure the correct packages are linked and put in the new lists.
    
    The current truck that is being sorted will be linked to the efficient lists and index list.
    
    Every time the lists are updated the smallest value is deleted from the distance list.
    
    The function will be called recursively and will update the current location.
    
    When the list of arguments is empty, the empty list will be returned and the call of the function will terminate.
    
    The specified truck is moved to its new position.
    
    This algorithm has a space-time complexity of O(N^2) because of the two loops and the repeated lookup function that
    is necessary to find the shortest path.   
    """

    def find_shortest_path(truck_package_list, truck_id, active_location):  # Section A
        if len(truck_package_list) == 0:  # Section B
            return truck_package_list
        else:  #
            try:
                smallest_value = 25.0
                next_location = 0
                for index in truck_package_list:
                    if check_current_distance(active_location, int(index[1])) <= smallest_value:
                        smallest_value = check_current_distance(active_location, int(index[1]))  # Section C
                        next_location = int(index[1])
                for index in truck_package_list:  # Section D
                    if check_current_distance(active_location, int(index[1])) == smallest_value:
                        if truck_id == 1:
                            efficient_truck_one.append(index)
                            index_list_truck_one.append(index[1])
                            pop_value = truck_package_list.index(index)
                            truck_package_list.pop(pop_value)
                            active_location = next_location
                            find_shortest_path(truck_package_list, 1, active_location)
                        elif truck_id == 2:
                            efficient_truck_two.append(index)
                            index_list_truck_two.append(index[1])
                            pop_value = truck_package_list.index(index)
                            truck_package_list.pop(pop_value)
                            active_location = next_location
                            find_shortest_path(truck_package_list, 2, active_location)
                        elif truck_id == 3:
                            efficient_truck_three.append(index)
                            index_list_truck_three.append(index[1])
                            pop_value = truck_package_list.index(index)
                            truck_package_list.pop(pop_value)
                            active_location = next_location
                            find_shortest_path(truck_package_list, 3, active_location)
            except IndexError:
                pass

    index_list_truck_one.insert(0, '0')

    """
    O(1) Space-Time Complexity
    """

    def optimal_index_truck_one():
        return index_list_truck_one

    """
    O(1) Space-Time Complexity
    """

    def optimal_list_truck_one():
        return efficient_truck_one

    index_list_truck_two.insert(0, '0')

    """
    O(1) Space-Time Complexity
    """

    def optimal_index_truck_two():
        return index_list_truck_two

    """
    O(1) Space-Time Complexity
    """

    def optimal_list_truck_two():
        return efficient_truck_two

    index_list_truck_three.insert(0, '0')

    """
    O(1) Space-Time Complexity
    """

    def optimal_index_truck_three():
        return index_list_truck_three

    """
    O(1) Space-Time Complexity
    """

    def optimal_list_truck_three():
        return efficient_truck_three
