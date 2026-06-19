import torch
import torch.nn.functional as F

def train(model, data, train_idx, epochs=100, lr=0.01):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()

        out = model(data)
        loss = F.nll_loss(out[train_idx], data.y[train_idx])

        loss.backward()
        optimizer.step()

        if epoch % 20 == 0:
            print(f"Epoch {epoch} | Loss: {loss.item():.4f}")

    return model
