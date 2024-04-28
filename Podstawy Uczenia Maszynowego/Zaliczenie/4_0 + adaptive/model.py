import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import pandas as pd
from pathlib import Path


use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")

# Data reading process

iris_df = pd.read_csv("iris.csv")
print('Data loader from CSV file, mapping values...')

# print(iris_df["variety"].unique())

# All data must be in number form, so we do mapping with variety
iris_df["variety"] = iris_df["variety"].map({'Setosa':0,'Versicolor':1,'Virginica':2})
print('All values has been mapped, prepping data..')

# print(iris_df.head())

# Prepraring data and target
X = iris_df.drop(["variety"],axis=1).values
y = iris_df["variety"].values

# print(X)

# Splitting it for train and test 70/30
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, stratify=y)

# print(train_X, train_y)

# Mapping it to tensors, adding to CPU or GPU
train_X = torch.FloatTensor(train_X).to(device)
test_X = torch.FloatTensor(test_X).to(device)
train_y = torch.LongTensor(train_y).to(device)
test_y = torch.LongTensor(test_y).to(device)


# Prepraring a custom dataset for this
class IrisDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]

train_dataset = IrisDataset(train_X, train_y)
test_dataset = IrisDataset(test_X, test_y)

# Hyperparams
LR = 0.001
BATCH_SIZE = 4
EPOCHS = 30
PATH = './iris.pth'


# Creating a data loader for easy iteration
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
print("Data correctly prepared")

# Creating our model, with 1 hidden layer and ReLU
class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        self.linear1 = nn.Linear(4, 128)
        self.linear2 = nn.Linear(128, 64)
        self.linear3 = nn.Linear(64, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.linear1(x))
        x = self.relu(self.linear2(x))
        x = self.linear3(x)
        return x
    

# Defining optimizer and loss fn
model = Classifier()
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(params=model.parameters(), lr=LR)


# Model training
def train():
    print('Starting training...')

    model.train()
    loss_values = []
     
    for i in range(1,EPOCHS+1):
        loss = 0.0
        for _, data in enumerate(train_loader):
            inputs, label = data

            optimizer.zero_grad()      
            pred = model(inputs)

            loss = criterion(pred, label)
            loss_values.append(loss)
            loss.backward()
            optimizer.step()

        if not i % 5:
            print(f"Epoch: {i} Train loss: {loss}")
    
    torch.save(model.state_dict(), PATH)
    print("Model saved")

# Model evaluation
def eval():
    print('Starting evaluation process...')

    model.eval()

    total_loss = 0
    correct_predictions = 0
    total_samples = 0
    with torch.no_grad():
        for _, data in enumerate(test_loader):
            inputs, label = data
            pred = model(inputs)
            loss = criterion(pred, label)
            total_loss += loss.item()
            _, predicted = torch.max(pred.data, 1)
            total_samples += label.size(0)
            correct_predictions += (predicted == label).sum().item()

    avg_loss = total_loss / len(test_loader)
    accuracy = correct_predictions / total_samples

    print(f"Test Loss: {avg_loss} Accuracy: {accuracy}")
    


if __name__ == "__main__":
    
    train()
    eval()
    # saved_path = Path(PATH)
    # if saved_path.is_file():
    #     # print("Found saved model, loading ...")
    #     model.load_state_dict(torch.load(PATH))
    #     eval()