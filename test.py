import math
from oneDimensionFunctions import *
from sympy import *

def targetFunc(x):
    # 目标函数
    return pow(x, 4) - 14 * pow(x, 3) + 60 * pow(x, 2) - 70 * x

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
cuttingLineMethod(targetFuncDiff, 13, 12, 1e-5)


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

