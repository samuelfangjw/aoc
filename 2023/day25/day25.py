import sys
import networkx as nx

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
G = nx.Graph()

with open(file) as f:
    for line in f:
        a,b = line.strip().split(': ')
        
        for c in b.split():
            G.add_edge(a,c)

cut_value, partition = nx.stoer_wagner(G)

part1 = len(partition[0]) * len(partition[1])
print(part1)
