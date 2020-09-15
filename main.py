import packages
from csvreader import get_hash_map
import datetime


class Main:
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('WGUPS Package Tracking System')
    print('Current delivery route was completed after', "{0:.2f}".format(packages.total_distance(), 2), 'miles.')
    start = input("To begin, please type 'search' to search for an individual package or "
                  "type 'time' to view the status of all packages at a specified time: ")
    # Space-time complexity is O(N)
    while start != 'exit':
        # if user types 'time' then they are prompted for a time to display. Once a time is provided it will
        # display all packages at that timestamp. Runtime of this process is O(N)
        if start == 'time':
            try:
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Space-time complexity is O(N^2)
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
                    # First checks all packages against the given time determine if they have left the hub yet.
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
                        # Then checks to see which packages have left the hub but have not been delivered yet
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
                        # Finally checks all packages that have already been delivered and displays the delivered time
                        else:
                            get_hash_map().get(str(count))[10] = 'Delivered at ' + time_two
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                            print('Package id:', get_hash_map().get(str(count))[0], '   Address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Delivery deadline:', get_hash_map().get(str(count))[6],
                                  ' Weight:', get_hash_map().get(str(count))[7],'  Truck status:',
                                  get_hash_map().get(str(count))[9],'  Delivery status:',
                                  get_hash_map().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Entry not valid.')
                exit()
        # If 'lookup' is selected than the user is prompted for a package ID followed by a timestamp
        # Once that information is entered then the user will be shown a particular package at a given time
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
                # First checks if the package has left the hub yet
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
                    # Then checks if the package has left the hub but has not been delivered yet
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
                    # If the package has already been delivered than it displays the time
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