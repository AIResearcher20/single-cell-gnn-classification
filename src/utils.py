import numpy as np
from sklearn.neighbors import kneighbors_graph

def build_graph(X, k=20):
    adj = kneighbors_graph(X, n_neighbors=k, mode='connectivity')
    edge_index = np.array(adj.nonzero())
    return edge_index
