import sys
import csv
import networkx as nx

def get_centrality(graph, centrality_measure, num_nodes):
    centrality_dict = {}
    if centrality_measure == "betweenness":
        centrality_dict = nx.betweenness_centrality(graph)
    elif centrality_measure == "closeness":
        centrality_dict = nx.closeness_centrality(graph)
    elif centrality_measure == "eigenvector":
        power_iterations = 100  #if takes too long to run, could reduce
        centrality_dict = nx.eigenvector_centrality(graph, power_iterations)
    elif centrality_measure == "harmonic":
        centrality_dict = nx.harmonic_centrality(graph)
    elif centrality_measure == "percolation":
        centrality_dict = nx.percolation_centrality(graph)
    elif centrality_measure == "degree":
        centrality_dict = nx.degree_centrality(graph)
    most_central_nodes = []
    i = 0
    for node in centrality_dict:
        i += 1
        if i >= num_nodes:  '''NEED TO SORT LIST''''
            break
        most_central_nodes.append(node)
    return most_central_nodes

def load_graph(file):
    with open(file, 'r', newline='') as csv:
        reader = csv.reader(csv, delimiter=',', quotechar='"')
        edges = []
        for row in reader:
            edge = (row[0], row[1])
            edges.append(edge)
    csv.close()
    graph = nx.MultiDiGraph(edges)
    return graph

def create_graph_from_dataset(node_list, start_graph, destination_file):
    '''Constructs a new graph from the file start_graph containing only
    the nodes in node_list. Writes the new graph into a csv file named
    filename.csv" with one edge per row.'''
    with open(start_graph, 'r', newline=''):
        reader = csv.reader(start_graph, delimiter=',', quotechar='"')
        with open(destination_file, 'w', newline='') as dest:
            writer = csv.writer(dest, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row[0] in node_list && row[1] in node_list:
                    writer.writerow(row)
        dest.close()
    start_graph.close()

def main():
    '''USAGE: python3 centrality.py graph_source centrality_measure,
    where centrality_measure is a string indicating which centrality type
    to calculate for the graph derived from file graph_source.'''
    graph_source = sys.argv[2]
    centrality_measure = sys.argv[3]
    graph = load_graph(graph_source)
    new_graph_size = 1000   #how of the most central nodes to include in new graph
    dest_file = "{}{}.csv".format(centrality_measure, new_graph_size)
    central_nodes = get_centrality(graph, centrality_measure, new_graph_size)
    create_graph_from_dataset(central_nodes, graph_source, dest_file)
