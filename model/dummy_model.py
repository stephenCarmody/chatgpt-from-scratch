import torch

class DummyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = torch.nn.Embedding(100, 100)
        self.linear = torch.nn.Linear(100, 100)

    def forward(self, x):
        return self.linear(self.embedding(x))
