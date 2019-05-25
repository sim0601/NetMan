import os
import sys
from prettytable import PrettyTable

file = 'bgp output'

with open(file, 'r') as f:
    for line in f:
        if 'BGP neighbor' in line:
            neig_data = line.split(' ')
            #print(neig_data)
            nei_IP = neig_data[3].split(',')
            #print(nei_IP[0])
            nei_AS = neig_data[7].split(',')
            #print(nei_AS[0])
        if 'BGP state' in line:
            state_data = line.split(' ')
            #print(state_data)
            state = state_data[5].split(',')
            #print(state[0])

            table = PrettyTable(["BGP neighbor IP", "BGP neighbor AS", "BGP neighbor state"])
            table.add_row([nei_IP[0], nei_AS[0],state[0]])
            print(table)
