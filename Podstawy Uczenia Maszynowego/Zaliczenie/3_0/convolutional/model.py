import torch
import torch.nn as nn
import torch.utils
from torchvision.transforms import ToTensor
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# CONV => RELU => POOL => FC => RELU => FC => SOFTMAX
class ConvNet(nn.Module):

    def __init__(self, channels, classes) -> None:
        super(ConvNet, self).__init__()

        self.relu = nn.ReLU()

        # First set of layers
        self.conv = nn.Conv2d(in_channels=channels, out_channels=20, kernel_size=(5,5))
        self.maxpool = nn.MaxPool2d(kernel_size=(2,2), stride=(2,2))

        # Why 2880? 28x28, kernel is 5x5 so the out after kernel will be 24x24, 
        # then maxpool (2x2) so the image is 2 times smaller, 
        # hence 64x144 for each out_channel (64 for batch size)(144*20=2880)

        # Linear layer
        self.fc1 = nn.Linear(in_features=2880, out_features=500)

        # Softmax classifier
        self.fc2 = nn.Linear(in_features=500, out_features=classes)
        self.soft = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = self.conv(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = self.relu(x)

        x = self.fc2(x)
        out = self.soft(x)

        return out


# Hyperparams
LR = 0.001
BATCH_SIZE = 64
EPOCHS = 5

TRAIN_SPLIT = 0.75
VAL_SPLIT = 1 - TRAIN_SPLIT
MODEL_PATH = 'model.pth'


# Using GPU for network calculations if possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Loading the dataset
print("Loading MNIST dataset..")
train_data = MNIST(root='data', train=True, download=True, transform=ToTensor())
test_data = MNIST(root='data', train=False, download=True, transform=ToTensor())

train_count = len(train_data)
test_count = len(test_data)

print(f'Train data count: {train_count}, Test data count: {test_count}')        # 60000 / 10000

# Splitting into training + validation + testing
new_train_count = int(train_count * TRAIN_SPLIT)
new_val_count = int(train_count * VAL_SPLIT)

(train_data, val_data) = torch.utils.data.random_split(train_data, [new_train_count, new_val_count],
                                                       generator=torch.Generator().manual_seed(52))
print('Data after splitting:')
print(f'Train data count: {len(train_data)}, Validation data count: {len(val_data)}, Test data count: {test_count}') 

# Creating data loaders for each dataset, shuffle is enabled for train set for better generalization
train_data_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
val_data_loader = DataLoader(val_data, batch_size=BATCH_SIZE)
test_data_loader = DataLoader(test_data, batch_size=BATCH_SIZE)

# Calculating steps for later model evaluation
train_steps = len(train_data_loader.dataset) // BATCH_SIZE
val_steps = len(val_data_loader.dataset) // BATCH_SIZE

# print(train_steps, val_steps)


# Model init channels=1 for grayscale, channels=3 for RGB, moving the model to CPU or GPU
model = ConvNet(channels=1, classes=len(train_data.dataset.classes)).to(device)

# Optimizer + Loss function
optimizer = torch.optim.Adam(model.parameters(), lr=LR)
loss_fn = nn.NLLLoss()

# Preparing a dictionary for learning history
H = {
    "train_loss": [],
    "train_acc": [],
    "val_loss": [],
    "val_acc": []
}
def train():
    for epoch in range(EPOCHS):
        model.train()       # Training mode for model

        # Variables for calculating accuracy later
        total_train_loss = 0
        total_val_loss = 0

        correct_train = 0
        correct_val = 0

        for (x, y) in train_data_loader:

            optimizer.zero_grad()

            (x, y) = (x.to(device), y.to(device))       # Value and class should be moved to CPU or GPU

            prediction = model(x)
            loss = loss_fn(prediction, y)
            loss.backward()
            optimizer.step()

            total_train_loss += loss
            correct_train += (prediction.argmax(1) == y).type(torch.float).sum().item()

            
        with torch.no_grad():

            model.eval()

            for (x, y) in val_data_loader:

                (x, y) = (x.to(device), y.to(device))

                prediction = model(x)
                
                total_val_loss += loss_fn(prediction, y)
                correct_val += (prediction.argmax(1) == y).type(torch.float).sum().item()


        avg_train_loss = total_train_loss / train_steps
        avg_val_loss = total_val_loss / val_steps

        correct_train = correct_train / len(train_data_loader.dataset)
        correct_val = correct_val / len(val_data_loader.dataset)

        H["train_loss"].append(avg_train_loss.cpu().detach().numpy())
        H["train_acc"].append(correct_train)
        H["val_loss"].append(avg_val_loss.cpu().detach().numpy())
        H["val_acc"].append(correct_val)

        print("[INFO] EPOCH: {}/{}".format(epoch + 1, EPOCHS))
        print("Train loss: {:.6f}, Train accuracy: {:.4f}".format(avg_train_loss, correct_train))
        print("Val loss: {:.6f}, Val accuracy: {:.4f}\n".format(avg_val_loss, correct_val))
            

    plot()
    torch.save(model, MODEL_PATH)

def test():

    print("Found saved model, evaluating on test set...")

    torch.load(MODEL_PATH)

    with torch.no_grad():

        model.eval()
        preds = []

        for (x, _) in test_data_loader:

            x = x.to(device)

            prediction = model(x)
            preds.extend(prediction.argmax(axis=1).cpu().numpy())


    print(classification_report(test_data.targets.cpu().numpy(),
	    np.array(preds), target_names=test_data.classes))
    
def plot():

    plt.style.use("ggplot")
    plt.figure()
    plt.plot(H["train_loss"], label="train_loss")
    plt.plot(H["val_loss"], label="val_loss")
    plt.plot(H["train_acc"], label="train_acc")
    plt.plot(H["val_acc"], label="val_acc")
    plt.title("Training Loss and Accuracy on Dataset")
    plt.xlabel("Epoch 5")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.show()



if __name__ == '__main__':

    # train()
    saved_file = Path(MODEL_PATH)
    if saved_file.is_file():
        test()

