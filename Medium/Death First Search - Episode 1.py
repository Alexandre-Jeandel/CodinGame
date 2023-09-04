import sys
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

list_of_links = [[] for _ in range(n)]  # List of lists to store links
list_gateway = []

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    list_of_links[n1].append(n2)
    list_of_links[n2].append(n1)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    list_gateway.append(ei)

def find_link_to_sever(start, exit_gateways, links):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)

        for neighbor in links[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [(current_node, neighbor)]))

            if neighbor in exit_gateways:
                return path + [(current_node, neighbor)]

    return None

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # Find the link to sever
    link_to_sever = find_link_to_sever(si, list_gateway, list_of_links)

    # Output the link to sever
    if link_to_sever:
        severed_link = link_to_sever[-1]
        print(link_to_sever[-1][0], link_to_sever[-1][1])

        # Remove the severed link from list_of_links
        list_of_links[severed_link[0]].remove(severed_link[1])
        list_of_links[severed_link[1]].remove(severed_link[0])