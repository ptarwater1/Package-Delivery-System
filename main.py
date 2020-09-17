"""
Patrick Tarwater #000919107
"""

import packages
from csvreader import get_hash_map
import datetime


class Main:
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('WGUPS Routing Program')
    print('Current delivery route was completed after', "{0:.2f}".format(packages.final_mileage(), 2), 'miles.')
    start = input("To begin, type 'search' to search for an individual package or "
                  "type 'time' to view the status of all packages at a specified time: ")

    """
    O(N) Space-Time Complexity
    """

    while start != 'exit':

        """
        The user types "time" and is asked to enter a time. When the time is entered, every package will be displayed at
        the given time.
        
        O(N) Runtime
        """

        if start == 'time':
            try:
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                """
                O(N^2) Space-Time Complexity
                """

                for count in range(1, 41):
                    try:
                        time_one = get_hash_map().get(str(count))[9]
                        time_two = get_hash_map().get(str(count))[10]
                        (h, m, s) = time_one.split(':')
                        time_one_conversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = time_two.split(':')
                        time_two_conversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass

                    """
                    Each package is checked to see if it has left the hub.
                    """

                    if time_one_conversion >= convert_user_time:
                        get_hash_map().get(str(count))[10] = 'At the Hub'
                        get_hash_map().get(str(count))[9] = 'Leaves at ' + time_one
                        print('Package id:', get_hash_map().get(str(count))[0], '  Address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Deadline:', get_hash_map().get(str(count))[6],
                              ' Weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    elif time_one_conversion <= convert_user_time:

                        """
                        Each package is checked to see if it has left the hub, if it has, checks if it has 
                        been delivered.
                        """

                        if convert_user_time < time_two_conversion:
                            get_hash_map().get(str(count))[10] = 'En route'
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                            print('Package id:', get_hash_map().get(str(count))[0], '  Address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Deadline:', get_hash_map().get(str(count))[6],
                                  ' Weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])

                            """
                            Packages that have been delivered are checked and returns the time it was delivered.
                            """

                        else:
                            get_hash_map().get(str(count))[10] = 'Delivered at ' + time_two
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                            print('Package id:', get_hash_map().get(str(count))[0], '  Address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Deadline:', get_hash_map().get(str(count))[6],
                                  ' Weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Entry not valid.')
                exit()
            """
            If the user enters "search", they are then asked to provide a package id. Then they are asked to specify
            a time which will display the specified package at the entered time.
            """

        elif start == 'search':
            try:
                count = input('Please enter package id to search: ')
                time_one = get_hash_map().get(str(count))[9]
                time_two = get_hash_map().get(str(count))[10]
                package_status_time = input('Time as HH:MM:SS : ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = time_one.split(':')
                time_one_conversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = time_two.split(':')
                time_two_conversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                """
                Determines if the package has departed the hub.
                """

                if time_one_conversion >= convert_user_time:

                    get_hash_map().get(str(count))[10] = 'At Hub'
                    get_hash_map().get(str(count))[9] = 'Leaves at ' + time_one
                    print('Package id:', get_hash_map().get(str(count))[0], '   Address:',
                          get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                          get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                          '  Delivery deadline:', get_hash_map().get(str(count))[6],
                          ' Weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                          get_hash_map().get(str(count))[9], '  Delivery status:',
                          get_hash_map().get(str(count))[10])
                elif time_one_conversion <= convert_user_time:

                    """
                    Determines if the package has departed the hub but is yet to be delivered.
                    """

                    if convert_user_time < time_two_conversion:
                        get_hash_map().get(str(count))[10] = 'En route'
                        get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                        print('Package id:', get_hash_map().get(str(count))[0], '   Address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Delivery deadline:', get_hash_map().get(str(count))[6],
                              ' Weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])

                        """
                        Determines what time the package has been delivered.
                        """

                    else:
                        get_hash_map().get(str(count))[10] = 'Delivered at ' + time_two
                        get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                        print('Package id:', get_hash_map().get(str(count))[0], '   Address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Delivery deadline:', get_hash_map().get(str(count))[6],
                              ' Weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
            except ValueError:
                print('Entry not valid.')
                exit()
        elif start == 'exit':
            exit()
        else:
            print('Entry not valid.')
            exit()