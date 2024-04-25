import torch 
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


# Model class
class XOR(nn.Module):
    
    def __init__(self):
        super(XOR, self).__init__()
        self.fc1 = nn.Linear(2, 4)
        self.fc2 = nn.Linear(4, 1)

    def forward(self, x):

        x = F.sigmoid(self.fc1(x))
        x = self.fc2(x)
        return x
    
# XOR data and targets
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

# Parsing data into torch tensors (tensor is just a word for multi dimentional vector)

inputs = torch.tensor(X, dtype=torch.float32)
targets = torch.tensor(y, dtype=torch.float32)

# print(inputs, type(inputs))

# Model init 
xor_net = XOR()

# Hyperparams block
lr = 0.01
epoch_count = 8000

# Loss and optimization functions
criterion = nn.MSELoss()
optimizer = optim.SGD(xor_net.parameters(), lr=lr)

print("Training....")

# We set the model to training mode
xor_net.train()

for epoch in range(1, epoch_count+1):

    for input, target in zip(inputs, targets):
        optimizer.zero_grad()           # Zeroing the gradients 
        out = xor_net(input)        # Getting the output from the network

        loss = criterion(out, target)        # Calculating the loss value from current output
        loss.backward()             # Back propagation
        optimizer.step()            # Update the weights


    if (epoch+1) % 1000 == 0:
        print(f'Epoch [{epoch+1}/{epoch_count}], Loss: {loss.item():.4f}')


# Setting into evaluation mode for validation
xor_net.eval()

print("")
print("Final results:")
for input, target in zip(inputs, targets):
    output = xor_net(input)
    print("Input:[{},{}] Target:[{}] Predicted:[{}] Error:[{}]".format(
        int(input.data.numpy()[0]),
        int(input.data.numpy()[1]),
        int(target.data.numpy()[0]),
        round(float(output.data.numpy()[0]), 4),
        round(float(abs(target.data.numpy()[0] - output.data.numpy()[0])), 4)
    ))





