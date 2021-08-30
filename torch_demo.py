import torch
import numpy as np

# x_data = torch.tensor([[1, 2], [3, 4]])
# x_data_1 = torch.ones_like(x_data)
# x_data_0 = torch.zeros_like(x_data)
# print(f'x_data: {x_data}')
# print(torch.ones_like(x_data))
# print(torch.rand_like(x_data, dtype=torch.float))
# print(torch.cat([x_data, x_data_0, x_data_1], dim=0))

# x = torch.ones(5)
# w = torch.randn(5, 3, requires_grad=True)
# b = torch.randn(3, requires_grad=True)
# z = torch.matmul(x, w) + b
# print(f'x: {x.grad_fn}')
# print(f'w: {w.grad_fn}')
# print(z.backward())
# print(f'x: {x.grad_fn}')
# print(f'w: {w.grad_fn}')

# inp = torch.eye(5, requires_grad=True)
# print(inp.grad_fn)
# out = (inp + 1).pow(2)
# out.backward(torch.ones_like(inp), retain_graph=True)
# print(inp.grad_fn)
# print('First call\n', inp.grad)
# out.backward(torch.ones_like(inp), retain_graph=True)
# print('Second call\n', inp.grad)
# print(inp.grad.zero_())

def targetFunction(x):
    Q = torch.tensor([[1.0, 0], [0, 2.0]])
    b = torch.tensor([1.0, 2.0])
    f = 0.5 * x.T.matmul(Q).matmul(x) + b.matmul(x)
    return f

x = torch.tensor([[1.0], [2.0]], requires_grad=True)
print(f'x = {x}')
z = targetFunction(x)
print(f'z = {z}')
z.backward()
print(f'x grad = {x.grad}')
print(x.shape)