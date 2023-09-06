"""
File: spider_web.py
Author: Alfonso Sebastian Apelacio Martinez
Date: 12/03/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

import random


def spider_web(web_map, starting_place, destination):
    visited = []
    pathway = spider_web_helper(web_map, starting_place, destination, visited)
    print(f"You visited {visited}")
    print(pathway)




# visited is a dictionary of where we have been
def spider_web_helper(web_map, current_place, destination, visited):
    # base cases
    if current_place == destination:
        visited.append(current_place)
        print(f"You have reached the destination at {destination}!")
        return destination

    #elif current_place in visited:
        #return

    elif current_place not in visited:
        # Recursive case
        visited.append(current_place)
        # Will traverse each node connected to
        # the node at starting_place
        for each_node in web_map[current_place]:
            print(web_map[current_place])
            if each_node not in visited:
                # makes a final_path list to track a path towards destination
                final_path = [spider_web_helper(web_map, each_node, destination, visited)]
                print(final_path)
                final_path.append(current_place)
                return final_path



def make_spider_web(num_nodes, seed=0):
    if seed:
        random.seed(seed)

    web_map = {}

    for i in range(1, num_nodes + 1):
        web_map[f'Node {i}'] = []

    for i in range(1, num_nodes + 1):
        sample = random.sample(list(range(i, num_nodes + 1)), random.randint(1, num_nodes - i + 1))
        print('sample', i, sample)
        for x in sample:
            if i != x:
                web_map[f'Node {i}'].append(f'Node {x}')
                web_map[f'Node {x}'].append(f'Node {i}')
    return web_map


def fixing_final_path(path_list):
    pass

if __name__ == '__main__':
    num_nodes, seed = [int(x) for x in input('Input num_nodes, seed: ').split(',')]
    the_web = make_spider_web(num_nodes, seed)
    print(spider_web(the_web, 'Node 1', f'Node {num_nodes}'))
