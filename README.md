# 🧬 Single-Cell RNA-seq Analysis using Graph Neural Networks (GCN & GAT)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/Deep%20Learning-Graph%20Neural%20Networks-orange)
![Scanpy](https://img.shields.io/badge/Single--Cell-Transcriptomics-green)
![Status](https://img.shields.io/badge/Research-Completed-brightgreen)
![Domain](https://img.shields.io/badge/Bioinformatics-AI%20for%20Genomics-purple)

---

## 🧠 Abstract

This project investigates the application of **Graph Neural Networks (GNNs)** for cell-type classification in single-cell RNA sequencing (scRNA-seq) data.

We construct a **k-nearest neighbor graph in PCA-reduced latent space**, enabling the modeling of **cell–cell interactions as a non-Euclidean structure**.

Two state-of-the-art architectures are evaluated:

- Graph Convolutional Networks (GCN)
- Graph Attention Networks (GAT)

---

## 🔬 Scientific Motivation

Traditional machine learning methods assume **independent and identically distributed (i.i.d.) samples**, which is invalid in biological systems.

Instead, cells exist in a **continuous transcriptional manifold**, where:

- Neighboring cells share functional similarity  
- Gene expression exhibits nonlinear structure  
- Local topology is biologically meaningful  

Graph-based learning directly addresses this limitation.

---

## 🧪 Methodology

### 🔷 Data Processing Pipeline

```text
Raw Counts → Normalization → Log Transform → HVG Selection → PCA → kNN Graph → GNN
🔷 Graph Construction
A k-nearest neighbor graph is constructed:
Nodes = cells
Edges = transcriptional similarity
Distance metric = Euclidean in PCA space
🔷 Models
🟦 GCN (Graph Convolutional Network)
Learns uniform neighborhood aggregation:
🟥 GAT (Graph Attention Network)
Introduces learnable attention weights:
👉 Enables adaptive importance weighting of neighboring cells.
📊 Experimental Setup
Dataset: PBMC single-cell RNA-seq
Dimensionality reduction: PCA (50 components)
Graph: kNN (k = 20)
Evaluation metrics:
Accuracy
Macro F1-score
Confusion Matrix
📈 Results
Model
Accuracy
Macro F1
Logistic Regression
~0.47
~0.34
GCN
~0.78
~0.66
GAT
~0.81
~0.67
🧬 Key Findings
GNNs significantly outperform classical ML methods
GAT consistently improves over GCN due to attention mechanism
Graph structure captures biologically meaningful relationships
📌 Conclusion
Graph-based deep learning provides a powerful framework for modeling:
Cellular heterogeneity
Transcriptional similarity
Non-Euclidean biological manifolds
GAT demonstrates superior performance by learning adaptive inter-cell dependencies.
🚀 Future Work
Integration with multi-omics data
Transformer-based graph models
Self-supervised pretraining on scRNA-seq
Spatial transcriptomics extension
📁 Repository Structure
Copy code
Text
src/        → core implementation  
models/     → trained models  
results/    → figures & plots  
docs/       → report & presentation
🧠 Keywords
Graph Neural Networks, scRNA-seq, Bioinformatics, Single-cell Analysis, GAT, GCN, PCA, kNN Graph
🏆 Project Status
✔ Completed
✔ Reproducible
✔ Research-grade implementation
✔ Suitable for academic submission
