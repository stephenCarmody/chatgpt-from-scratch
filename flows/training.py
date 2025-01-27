import argparse
import os

import torch
import torch.nn as nn
import torch.optim as optim

from model.simple_model import SimpleNet


def train(epochs, model_dir):
    # Create dummy data
    X = torch.randn(100, 10)
    y = torch.randint(0, 2, (100,))

    # Initialize the model
    model = SimpleNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Training loop
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

    # Save the model
    torch.save(model.state_dict(), os.path.join(model_dir, "model.pth"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Sagemaker specific arguments
    parser.add_argument(
        "--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR", "./artifacts")
    )
    parser.add_argument(
        "--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN", "./")
    )
    parser.add_argument("--epochs", type=int, default=100)

    args = parser.parse_args()

    # Always run training - whether local or on SageMaker
    train(epochs=args.epochs, model_dir=args.model_dir)
