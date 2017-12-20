import re

def process_input(file_name):
    connections_dict = {}
    with open(file_name) as f:
        r = re.compile('(\d+)+\s<->\s(.*)$')
        for l in f:
            (node, arr_str) = r.search(l).groups()
            arr = arr_str.replace(' ', '').split(',')
            connections_dict[node] = arr
    
    return connections_dict

def gen_connections(node, connections_dict, connected_nodes):
    connected_nodes.add(node)
    connections = connections_dict[node]
    for c in connections:
        if c not in connected_nodes:
            gen_connections(c, connections_dict, connected_nodes)
    
def contained_in_any_group(node, group_arr):
    for group in group_arr:
        if node in group:
            return True
    return False

def num_groups(connections_dict):
    groups = []
    connected_nodes = set()
    for key in connections_dict.keys():
        if not contained_in_any_group(key, groups):
            connected_nodes = set()
            gen_connections(key, connections_dict, connected_nodes)
            groups.append(connected_nodes)
    return len(groups)

            
if __name__ == '__main__':
    file_name = 'input12.txt'
    connections_dict = process_input(file_name)
    connected_nodes = set()
    gen_connections('0', connections_dict, connected_nodes)
    print('Result part 1: {0}'.format(len(connected_nodes)))
    print('Result part 2: {0}'.format(num_groups(connections_dict)))
            
