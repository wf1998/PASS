import torch
from torch import nn
from torch.nn import MaxPool2d

input = torch.tensor([[1,2,0,3,1],
                      [0,1,2,3,1],
                      [1,2,1,0,0],
                      [5,2,3,1,1],
                      [2,1,0,1,1]],dtype=torch.float32)
input = torch.reshape(input,(-1,1,5,5))
print(input.shape)
print(input)

class ss(nn.Module):
    def __init__(self):
        super(ss,self).__init__()
        self.maxpool1 = MaxPool2d(3,ceil_mode=True)
    def forward(self,input):
        output = self.maxpool1(input)
        return output
ssy = ss()
output = ssy(input)
print(output)