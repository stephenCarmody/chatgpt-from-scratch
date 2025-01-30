import math

import torch
import torch.nn as nn


def GELU(x):
    """
    Gaussian Error Linear Unit
    Paper: http://arxiv.org/pdf/1606.08415
    Why it works better than ReLU: http://arxiv.org/pdf/1606.08415#page=6
        GELUs work better than ReLU because they offer more curvature and non-monotonicity
        at all points, allowing them to better approximate complex functions. Additionally,
        GELUs have a probabilistic interpretation and weight inputs based on their relative
        magnitude rather than just gating based on sign like ReLU does.
    """
    return (
        0.5
        * x
        * (1 + torch.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * torch.pow(x, 3))))
    )


class CausalSelfAttention(nn.Module):
    def __init__(self, config):
        pass

    def forward(self, x):
        pass


class Block(nn.Module):
    def __init__(self, config):
        pass

    def forward(self, x):
        pass


class GPT2(nn.Module):
    def __init__(self, config):
        pass

    def forward(self, x):
        pass

    @torch.no_grad()
    def generate(self, prompt, max_length, temperature=1.0, top_k=None, top_p=None):
        pass
