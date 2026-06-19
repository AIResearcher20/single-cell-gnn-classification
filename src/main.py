import torch
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from torch_geometric.data import Data

from data_loader import load_data
from models import GAT
from utils import build_graph
from train import train

# ---------------- DEVICE ----------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------- DATA ----------------
adata, X = load_data()

labels = adata.obs["louvain"] if "louvain" in adata.obs else adata.obs.iloc[:, 0]

le = LabelEncoder()
y = le.fit_transform(labels)

# ---------------- SPLIT ----------------
train_idx, test_idx = train_test_split(
    np.arange(len(y)),
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ---------------- GRAPH ----------------
edge_index = build_graph(X, k=20)

data = Data(
    x=torch.tensor(X, dtype=torch.float),
    edge_index=torch.tensor(edge_index, dtype=torch.long),
    y=torch.tensor(y, dtype=torch.long)
).to(device)

train_idx = torch.tensor(train_idx, dtype=torch.long).to(device)
test_idx = torch.tensor(test_idx, dtype=torch.long).to(device)

# ---------------- MODEL ----------------
model = GAT(
    in_dim=X.shape[1],
    hidden=32,
    out_dim=len(np.unique(y))
).to(device)

# ---------------- TRAIN ----------------
model = train(model, data, train_idx)

# ---------------- EVAL ----------------
model.eval()

with torch.no_grad():
    pred = model(data).argmax(dim=1).cpu().numpy()

acc = accuracy_score(y[test_idx.cpu()], pred[test_idx.cpu()])
f1 = f1_score(y[test_idx.cpu()], pred[test_idx.cpu()], average="macro")

print("\n===== FINAL RESULTS =====")
print("Accuracy:", acc)
print("Macro F1:", f1)
