import csv
import datetime

with open('addresses.csv') as csvfile:
    csv_addresses = csv.reader(csvfile, delimiter=',')
    csv_addresses = list(csv_addresses)

with open('distances.csv') as csvDistance:
    csv_distances = csv.reader(csvDistance, delimiter=',')
    csv_distances = list(csv_distances)

    def inspect_distance(row_value, column_value, distance_sum):
        distance = csv_distances[row_value][column_value]
        if distance is '':
            distance = csv_distances[column_value][row_value]

        distance_sum += float(distance)
        return distance_sum




