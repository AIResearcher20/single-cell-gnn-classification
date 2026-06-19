import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, GATConv

class GCN(torch.nn.Module):
    def __init__(self, in_dim, hidden, out_dim):
        super().__init__()
        self.conv1 = GCNConv(in_dim, hidden)
        self.conv2 = GCNConv(hidden, out_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)


class GAT(torch.nn.Module):
    def __init__(self, in_dim, hidden, out_dim):
        super().__init__()
        self.gat1 = GATConv(in_dim, hidden, heads=4, concat=True)
        self.gat2 = GATConv(hidden * 4, out_dim, heads=1)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.elu(self.gat1(x, edge_index))
        x = self.gat2(x, edge_index)
        return F.log_softmax(x, dim=1)
