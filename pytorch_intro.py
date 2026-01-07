import torch

# Create a tensor
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Perform a simple operation (matrix multiplication)
y = x.matmul(x.T)

# Check if a GPU is available
device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(f"Tensor on {device}:")
print(y)

# Expected Output (on CPU):
# Tensor on cpu:
# tensor([[ 5., 11.],
#         [11., 25.]])
