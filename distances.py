import csv
import datetime

# Read in csv file that is the names of all possible delivery locations
with open('addresses.csv') as csv_name_file:
    csv_addresses = csv.reader(csv_name_file, delimiter=',')
    csv_addresses = list(csv_addresses)

# Read in csv file that is the mapping of distances between locations
with open('distances.csv') as csvfile:
    csv_distances = csv.reader(csvfile, delimiter=',')
    csv_distances = list(csv_distances)

    # a list of row/column values are inserted into this function. This function then calculates the total distance
    # that distance is then returned and each iteration represents a distance between two locations
    # Space-time complexity is O(1)
    def distance_inspection(row_value, column_value, distance_sum):
        distance = csv_distances[row_value][column_value]
        if distance == '':
            distance = csv_distances[column_value][row_value]

        distance_sum += float(distance)
        return distance_sum

    # this function is very similar to the function above but returns a current distance
    # Space-time complexity is O(1)
    def check_current_distance(row_value, column_value):
        distance = csv_distances[row_value][column_value]
        if distance == '':
            distance = csv_distances[column_value][row_value]
        return float(distance)
    # this is the time that the first truck leaves the hub
    first_time_list = ['8:00:00']
    second_time_list = ['9:05:00']
    third_time_list = ['11:00:00']

    # this function takes a distance then divides it by 18. It then uses divmod to display a time and appends 00
    # this string that is a timestamp is then split and turned into a datetime timedelta object
    # that object is then added to sum which represents total distance for a particular truck
    # runtime of function is O(N)
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

    # Repeated function for second truck
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

    # Repeated function for the third truck
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

    # this function returns the time objects to use in the packages.py file
    # Space-time complexity is O(1)
    def address_check():
        return csv_addresses
    # these lists represent the sorted trucks that are put in order of efficiency in the function below
    efficient_truck_one = []
    index_list_truck_one = []
    efficient_truck_two = []
    index_list_truck_two = []
    efficient_truck_three = []
    index_list_truck_three = []

    # This is my sorting algorithm that uses a greedy approach to automate optimizing the delivery route for each truck.
    # the function takes 3 parameters (see section 1)
    # First parameter is the list of packages on a truck that has not been optimized yet
    # The second parameter represents the truck number
    # The third parameter represents the current location that is updated each time a truck moves

    # The base case of the algorithm is stated in the initial if statement (see section 2). This breaks the recursion
    # once the input list has a size of 0.
    # It starts by setting a "lowest value" of 50.0 and then uses the check current distance function to loop through
    # every possible point that is currently available to see if there is a lower value. If there is than the lowest
    # value is updated and the search continues (see section 3). Once it has searched through all possible routes
    # the truck can go given the available packages, it then adds that package object and associated index to
    # new lists (see section 4). To ensure that the right truck packages are being associated, the second parameter
    # is checked. If the truck truck is being sorted than the optimized delivery path will be associated to the lists
    # first_optimized_truck and first_optimized_truck_index. Each time these lists are updated, the lowest value is
    # removed from the argument list, truck_distance_list. This will allow us to update current location and recursively
    # call the function. Once the argument list is empty it will return the empty list and the function call will end.

    # The space-time complexity of this algorithm is O(N^2). This is due to the two for loops and the repeated lookup
    # functionality required to determine the lowest possible path then move the truck to that position.

    def find_shortest_path(truck_distance_list, truck_number, current_location):  # section 1
        if len(truck_distance_list) == 0:  # section 2
            return truck_distance_list
        else:  #
            try:
                lowest_value = 25.0
                new_location = 0
                for index in truck_distance_list:
                    if check_current_distance(current_location, int(index[1])) <= lowest_value:
                        lowest_value = check_current_distance(current_location, int(index[1]))  # section 3
                        new_location = int(index[1])
                for index in truck_distance_list:  # section 4
                    if check_current_distance(current_location, int(index[1])) == lowest_value:
                        if truck_number == 1:
                            efficient_truck_one.append(index)
                            index_list_truck_one.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            find_shortest_path(truck_distance_list, 1, current_location)
                        elif truck_number == 2:
                            efficient_truck_two.append(index)
                            index_list_truck_two.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            find_shortest_path(truck_distance_list, 2, current_location)
                        elif truck_number == 3:
                            efficient_truck_three.append(index)
                            index_list_truck_three.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            find_shortest_path(truck_distance_list, 3, current_location)
            except IndexError:
                pass

    index_list_truck_one.insert(0, '0')

    # Space-time complexity is O(1)
    def optimal_index_truck_one():
        return index_list_truck_one

    # Space-time complexity is O(1)
    def optimal_list_truck_one():
        return efficient_truck_one

    index_list_truck_two.insert(0, '0')

    # Space-time complexity is O(1)
    def optimal_index_truck_two():
        return index_list_truck_two

    # Space-time complexity is O(1)
    def optimal_list_truck_two():
        return efficient_truck_two

    index_list_truck_three.insert(0, '0')

    # Space-time complexity is O(1)
    def optimal_index_truck_three():
        return index_list_truck_three

    # Space-time complexity is O(1)
    def optimal_list_truck_three():
        return efficient_truck_three
