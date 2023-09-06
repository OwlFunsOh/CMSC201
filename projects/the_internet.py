"""
File:    the_internet.py
Author:  Alfonso Sebastian Apelacio Martinez
Date:    12/01/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

# creates servers within the internet
def create_server(server_name, ip_address, dictionary_of_servers):
    # Boolean flag to see if ip_address is unique
    is_unique = True

    # The loop below checks every server to see if the ip_address you want to add
    # is already in the list of ip_addresses
    for each_server in dictionary_of_servers:
        if dictionary_of_servers[each_server]["ip-address"] == ip_address:
            print(f"The ip_address you entered for {server_name} matches with \n"
                  f"{each_server}! Cannot add server")
            is_unique = False

    # Boolean flag to check if ip address is legal
    is_valid = True

    # The following splits the address into its parts
    # and compares the numbers to see if they are within
    # the bounds.
    ip_address_parts = ip_address.split(".")
    if len(ip_address_parts) != 4:
        is_valid = False
    for each_address in ip_address_parts:
        if int(each_address) > 255 or int(each_address) < 0:
            print(f"The ip address {ip_address} is invalid.")
            is_valid = False


    if is_unique and is_valid:
        dictionary_of_servers[server_name] = {}
        dictionary_of_servers[server_name]["ip-address"] = ip_address

    return dictionary_of_servers



# Creates connections and saves them to the dictionary
def create_connection(server_1, server_2, connection_time, dictionary_of_servers):
    if server_1 in dictionary_of_servers and server_2 in dictionary_of_servers:
        # adds the connection time to both servers since it connects 2 ways
        dictionary_of_servers[server_1]["connected-servers"] = {}
        dictionary_of_servers[server_1]["connected-servers"][server_2] = connection_time

        dictionary_of_servers[server_2]["connected-servers"] = {}
        dictionary_of_servers[server_2]["connected-servers"][server_1] = connection_time


    return dictionary_of_servers


# sets your location to the server defined by server_credentials
# server credentials can either be ip-address or domain name
def set_server(server_credentials, dictionary_of_servers):
    # checks each server then sees if the ip-address or name matches anywhere
    for each_server in dictionary_of_servers:
        if each_server == server_credentials or dictionary_of_servers[each_server]["ip-address"] == \
                server_credentials:
            print(f"Your location is now at {each_server}")
            return each_server
    print(f"No server was found with {server_credentials}.")
    return ""


# displays current location if you set one
def ip_config(server_credentials, dictionary_of_servers):
    if len(server_credentials) != 0:
        print(f"You are currently at {server_credentials}\t{dictionary_of_servers[server_credentials]['ip-address']}")
        return True

    else:
        print("You have not set a server")
        return False



# gives global view of all the servers
def display_servers(dictionary_of_servers):
    for each_server in dictionary_of_servers:
        print(f"{each_server} \t {dictionary_of_servers[each_server]['ip-address']}")
        if "connected-servers" in dictionary_of_servers[each_server]:
            for each_connected_server in dictionary_of_servers[each_server]["connected-servers"]:
                print(f"\t {each_connected_server} \t {dictionary_of_servers[each_connected_server]['ip-address']} \t "\
                      f"{dictionary_of_servers[each_server]['connected-servers'][each_connected_server]}")

def traceroute(dictionary_of_servers):
    pass


# The following functions will see how long it will take to get to the end function
def ping_server(dictionary_of_servers, starting_server, destination_server):

    server_is_set = ip_config(starting_server, dictionary_of_servers)
    if server_is_set:
        visited_dictionary = {}

        for each_server in dictionary_of_servers:
            visited_dictionary[each_server] = False

        # The following will create a server dictionary that checks if you visited it
        ping_time = ping_server_helper(starting_server, destination_server, dictionary_of_servers, visited_dictionary, 0)
        print(f"Reply from {dictionary_of_servers[destination_server]['ip-address']} = {ping_time}ms")


# The following is the recursive function to check for paths
def ping_server_helper(current_server, destination_server, dictionary_of_servers, visited_dict, current_ping):
        # base case
        if current_server == destination_server:
            visited_dict[destination_server] = True
            return current_ping

        else:
            # recursive case
            visited_dict[current_server] = True
            # The following will traverse each server connected to the current server
            for each_connected_server in dictionary_of_servers[current_server]["connected-servers"]:
                if visited_dict[each_connected_server] == False:
                    adding_ping = ping_server_helper(each_connected_server, destination_server, dictionary_of_servers, visited_dict, current_ping + int(dictionary_of_servers[current_server]\
                        ["connected-servers"][each_connected_server]))
                    return adding_ping


# this function will trace where we went through to ping the server
def traceroute(server_credentials, dictionary_of_servers):
    pass






if __name__ == "__main__":
    # The following will be the dictionary of servers
    server_dictionary = {}

    # The following is where the user currently is
    user_location = ""

    # Takes the command the user types in
    user_command = input(">>> ")

    while user_command.lower() != "quit":
        # Below splits the command so we can put it in our function parameters
        command = user_command.split()

        if command[0].lower() == "create-server":
            create_server(command[1], command[2], server_dictionary)

        elif command[0].lower() == "create-connection":
            create_connection(command[1], command[2], command[3], server_dictionary)

        elif command[0].lower() == "set-server":
            user_location = set_server(command[1], server_dictionary)

        elif command[0].lower() == "ip-config":
            ip_config(user_location, server_dictionary)

        elif command[0].lower() == "display-servers":
            display_servers(server_dictionary)

        elif command[0].lower() == "ping":
            ping_server(server_dictionary, user_location, command[1].lower())


        print(server_dictionary)

        #asks for user input again
        user_command = input(">>> ")

