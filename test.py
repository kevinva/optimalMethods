import math
from oneDimensionFunctions import *
from gradientMethods import *
from sympy import *
import torch

def targetFunc(x):
    # 目标函数
    return pow(x, 4) - 14 * pow(x, 3) + 60 * pow(x, 2) - 70 * x

def targetFuncv2(x: torch.Tensor):
    Q = torch.tensor([[1, 0], [0, 1]], dtype=torch.float)
    return x.T.matmul(Q).matmul(x)

def targetFuncDiff(xVal, diffCount):
    # 求函数的导数
    x = symbols('x')
    # targetFuncExpr = 0.5 * x ** 2 - sin(x)
    targetFuncExpr = pow(x, 3) - 12.2 * pow(x, 2) + 7.45 * x + 42
    exprDiff = diff(targetFuncExpr, x, diffCount)
    return targetFuncExpr.subs(x, xVal), exprDiff.subs(x, xVal)

# goldenCutMethod(0, 2, 0.3, targetFunc)
# fibonacciMethod(0, 2, 0.3, targetFunc, 0.05)
# newtonMethod(targetFuncDiff, 1e-6, 0.5)
# cuttingLineMethod(targetFuncDiff, 13, 12, 1e-5)
# findMiniPointBoundaryForFunction(targetFunc)


##################################  sympy demo ###############################
# x = symbols('x')
# expr = cos(x) + 1
# print(expr.subs(x, 0))

# x, y, z = symbols('x y z')
# # expr = pow(x, 3) + 4 * x * y - z
# # print(expr.subs([(x, 2), (y, 4), (z, 0)]))
# # print(limit(1 / x, x, 0))
# expr = pow(x, 3)
# # print(diff(sin(x), x))
# # print(diff(pow(x, 2), x, 2))
# expr_diff = diff(expr, x, 2)
# print(expr_diff.subs([(x, 2)]))

# x = torch.tensor([[4], [2]], dtype=torch.float)
# a = torch.tensor([1.23], requires_grad=True)
# x_new = a * x
# f = targetFuncv2(x_new)
# f.backward()
# print(a.grad)
# print(x.grad)
# x = torch.randn(3, requires_grad=True)
# x1 = torch.tensor(x)
# print(x)
x = torch.tensor([[4], [2]], requires_grad=True, dtype=torch.float)
fastestGradient(targetFuncv2, x)