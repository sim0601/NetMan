from prettytable import PrettyTable

file = 'ospfdata.txt'

with open(file, 'r') as f:
    for line in f:

        id = []
        #print(line)

        if 'Neighbor ID' in line:
            title = line.split(' ')
            print(title[0], title[1], title[9].rjust(11), title[33].strip('\n').rjust(14))

        if '10.0.0.1' in line:
            data1 = line.split(' ')
            print(data1[0], data1[13].rjust(16),data1[25].rjust(18))
            id.append(data1[0])
            #print(id)

        if '20.0.0.1' in line:
            data2 = line.split(' ')
            print(data2[0], data2[13].rjust(17), data2[27].rjust(18))
            id.append(data2[0])

        if '30.0.0.1' in line:
            data3 = line.split(' ')
            print(data3[0], data3[13].rjust(17), data3[31].rjust(18))


        if '40.0.0.1' in line:
            data4 = line.split(' ')
            print(data4[0], data4[13].rjust(16), data4[30].rjust(18))

        #print(id)

        '''table = PrettyTable(["Neighbor ID", "State", "Interface"])
            table.add_row([nei_IP[0], nei_AS[0],state[0]])
            print(table)'''
