import torch
from torch.autograd import grad

def fastestGradient(targetFunc, x0: torch.Tensor, eps=0.01):
    x = x0

    while True:
        f = targetFunc(x)
        f.backward()
        print(f'dx = {x.grad}')

        a1 = torch.randn(1, requires_grad=True)
        a2 = torch.randn(1, requires_grad=True)
        while True:
            x_new1 = x.detach() - a1 * x.grad
            x_new2 = x.detach() - a2 * x.grad
            # print(f'x_new = {x_new}')
            f_a1 = targetFunc(x_new1)
            f_a2 = targetFunc(x_new2)
            f_a1.backward()
            f_a2.backward()
            # print(f'da = {a.grad}')
            
            a_next = a2.grad * a1 - a1.grad * a2 / (a2.grad - a1.grad)  # 用割线法求关于a的极小点
            print(f'next a = {a_next}')
            
            x_temp = x.detach() - a_next.detach() * x.grad
            f_a_next = targetFunc(x_temp)
          
            if abs(f_a_next) < eps:
                break
            else:
                a1 = a2
                a2 = a_next

            break
    
        x_next = x.detach() - a2 * x.grad
        f_next = targetFunc(x_next)
        print(f'f_next = {f_next}')
        
