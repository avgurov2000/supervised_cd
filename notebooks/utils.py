import re
from typing import NamedTuple, Dict, List, Tuple
from collections import defaultdict

import numpy as np
import networkx as nx
import igraph as ig

import leidenalg
import math

from sklearn.metrics import normalized_mutual_info_score
from tqdm.notebook import tqdm


def nxBuildGraph(
    multiplex_list: Dict[int, List[List[int]]]
) -> List[nx.Graph]:
    """
    Transform multiplex networck from Dict[layer_number:int, List[edges:List[node_id:int, node_id:int]]]
    to form of List[networkx.Graph]
    
        Agruments:
            -- multiplex_list: Dict[int, List[List[int]]] is a dictionary, where key is a layer_number, value is a list of 
                               edges which is also a list of two nodes.
        Return:
            -- graphs_list_sorted: List[nx.Graph]
    """
    graphs_list = []
    graphs_levels = []
    all_nodes = set()
    
    for graph_level in multiplex_list:
        level = np.array(multiplex_list[graph_level])
        nodes = set(level[:, 0]).union(set(level[:, 1]))
        all_nodes = all_nodes.union(nodes)

    for graph_level in multiplex_list:
        level = np.array(multiplex_list[graph_level])
        g = nx.Graph()
        g.add_nodes_from(all_nodes)
        
        u_less_v = level[level[:, 0] < level[:, 1]]
        u_biger_v = level[level[:, 0] > level[:, 1]]
        
        g.add_edges_from(u_less_v, weight = 1)
        for edge in u_biger_v:
            u, v = edge[0], edge[1]
            if g.has_edge(v, u):
                g[v][u]['weight'] += 1
            else:
                g.add_edge(v, u, weight=1)
        
        graphs_list.append(g)
        graphs_levels.append(graph_level)
        
    
    graphs_list_sorted = [x for _, x in sorted(zip(graphs_levels, graphs_list))]
    return graphs_list_sorted


def from_ig_to_nx_partition_multiplex(
    partition_ig, 
    graph_ig
):
    """
    Transform a partitions return of igraph graph to the partition of networkx.Graph
    """
    partition_nx = {list(graph_ig.vs)[node]['_nx_name']: com for node, com in enumerate(partition_ig)}
    return partition_nx


def from_part_to_list(partition):
    """
    Transform a partition of networkx.Graph to ordered list
    """
    vs_list = []
    idx_list = []
    for _, i in enumerate(partition):
        for vs in i:
            vs_list.append(vs)
            idx_list.append(_)
    
    idx_list_sorted = [x for _, x in sorted(zip(vs_list, idx_list))]
    return idx_list_sorted


def fusion_graph(graphs, koeff):
    """
    Fusion several networkx.Graph's to one networkx.Graph
    """
    adj_matrixes = [nx.adjacency_matrix(i, i.nodes()) for i in graphs]
    alpha_adj_matrixes = [i*j for i,j in zip(adj_matrixes, koeff)]
    
    adj_for_graph = alpha_adj_matrixes[0]
    for i in range(1, len(alpha_adj_matrixes)):
        adj_for_graph += alpha_adj_matrixes[i]
        
    alpha_graph = nx.from_scipy_sparse_matrix(adj_for_graph, parallel_edges=False, edge_attribute='weight')
    alpha_graph_ig = ig.Graph.from_networkx(alpha_graph)

    return alpha_graph_ig