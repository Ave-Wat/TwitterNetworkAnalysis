import sys
import csv
import networkx as nx

def get_centrality(graph, centrality_measure, num_nodes):
    print("getting centrality...")

    centrality_dict = {}
    if centrality_measure == "betweenness":
        centrality_dict = nx.betweenness_centrality(graph)
    elif centrality_measure == "closeness":
        centrality_dict = nx.closeness_centrality(graph)
    elif centrality_measure == "eigenvector":
        power_iter = 100  #if takes too long to run, could reduce
        centrality_dict = nx.eigenvector_centrality(graph, max_iter=power_iter)
    elif centrality_measure == "harmonic":
        centrality_dict = nx.harmonic_centrality(graph)
    elif centrality_measure == "percolation":
        centrality_dict = nx.percolation_centrality(graph)
    elif centrality_measure == "degree":
        centrality_dict = nx.in_degree_centrality(graph)
    else:
        print("Invalid centrality measure")
        exit(0)
    print("got centrality!")

    central_nodes = sorted(centrality_dict.keys(), key=centrality_dict.get, reverse=True)
    return central_nodes[:num_nodes]

def load_graph(graph_source):
    print("loading graph")
    with open(graph_source, 'r', newline='') as gfile:
        reader = csv.reader(gfile, delimiter=',', quotechar='"')
        edges = []
        next(reader)
        for row in reader:
            edge = (row[0], row[1])
            edges.append(edge)
    gfile.close()
    graph = nx.DiGraph(edges)
    return graph

def create_graph_from_dataset(node_list, start_graph, destination_file):
    '''Constructs a new graph from the file start_graph containing only
    the nodes in node_list. Writes the new graph into a csv file named
    filename.csv" with one edge per row.'''
    print("writing new graph to file")
    with open(start_graph, 'r', newline='') as src:
        reader = csv.reader(src, delimiter=',', quotechar='"')
        with open(destination_file, 'w', newline='') as dest:
            writer = csv.writer(dest, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(next(reader))
            for row in reader:
                if row[0] in node_list and row[1] in node_list:
                    writer.writerow(row)
        dest.close()
    src.close()
    return

def main():
    '''USAGE: python3 centrality.py graph_source centrality_measure,
    where centrality_measure is a string indicating which centrality type
    to calculate for the graph derived from file graph_source.'''
    graph_source = sys.argv[1]
    centrality_measure = sys.argv[2]
    graph = load_graph(graph_source)
    new_graph_size = 1000   #how of the most central nodes to include in new graph
    dest_file = "data/{}{}.csv".format(centrality_measure, new_graph_size)
    central_nodes = get_centrality(graph, centrality_measure, new_graph_size)
    create_graph_from_dataset(central_nodes, graph_source, dest_file)
    exit(0)

if __name__ == "__main__":
    main()
