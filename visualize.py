import csv
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network
from sympy import false, true


# networkX config
G = nx.Graph()
pos = nx.spring_layout(G)

# load NIC / Vnet / Subnet Data to NetworkX
with open('export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for x in range(1):
        next(csv_reader)

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            ## networkx will avoid duplicate nodes, so load away!

            # add the Virtual network and Subnets w/ with their relationship
            VnetDataCard = f'rg:" {row[4]} "\n env: "Azure" \n type: VNET'

            G.add_node(str(row[0]), group=1, title=VnetDataCard, shape='image', image="./resources/Icons/networking/10061-icon-service-Virtual-Networks.svg")

            SubnetDataCard = f'rg:" {row[4]} "\n env: "Azure" \n type: Subnet'
            G.add_node(str(row[1]), group=2, title=SubnetDataCard,  shape='image', image="./resources/Icons/networking/10075-icon-service-Virtual-Networks-(Classic).svg")
            G.add_edge(str(row[0]), str(row[1]))
            
            # add the subnet, IP, VM Name and their relationship
            VmDataCard = f'rg:" {row[4]} "\n IP:" {row[2]} "\n env: "Azure" \n type: VM'
            G.add_node(str(row[3]), title=VmDataCard, group=3, shape='image', image='./resources/Icons/compute/10021-icon-service-Virtual-Machine.svg')
            G.add_edge(row[1],row[3])

            line_count += 1

print(f'Processed {line_count} Network Relationships.')


# load Vnet Peering to NetworkX

if (True):
    with open('export1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for x in range(1):
            next(csv_reader)

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                ## networkx will avoid duplicate nodes, so load away!

                # add peer node Data
                PeeringDataCard = f'name: {row[0]} \n rg:" {row[3]} "\n env: "Azure" \n type: Vnet Peering Rule'
                #G.add_node(str(row[0]), group=4, title=PeeringDataCard, shape='dot', label=" ")

                # add vnet node a
                VnetDataCard = f'rg:" {row[3]} "\n env: "Azure" \n type: VNET'
                G.add_node(str(row[1]), group=1, title=VnetDataCard, shape='image', image="./resources/Icons/networking/10061-icon-service-Virtual-Networks.svg")
                
                # add vnet node b
                VnetDataCard = f'rg:" {row[3]} "\n env: "Azure" \n type: VNET'
                G.add_node(str(row[2]), group=1, title=VnetDataCard, shape='image', image="./resources/Icons/networking/10061-icon-service-Virtual-Networks.svg")

                # add relationships
                G.add_edge(row[1],row[2], title=PeeringDataCard, width=2)
                #G.add_edge(row[0],row[2], title=PeeringDataCard, width=2)

                line_count += 1
    print(f'Processed {line_count} Vnet Peering Relationships.')


# find disjoint subgraphs

if (True):
    sub_graphs = (G.subgraph(c).copy() for c in nx.connected_components(G))
    for i, sg in enumerate(sub_graphs):
        print ("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))


# display Graph

net = Network(notebook=True, height='100%', width='100%')
net.toggle_physics(True)
#net.show_buttons(filter_=['physics', 'nodes', 'edges'])
net.from_nx(G)
net.show("example.html")


    