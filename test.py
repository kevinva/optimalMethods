import math
from oneDimensionFunctions import *


def targetFunc(x):
    return pow(x, 4) - 14 * pow(x, 3) + 60 * pow(x, 2) - 70 * x

# goldenCutWithRange(0, 2, 0.3, targetFunc)
fibonacciWithRange(0, 2, 0.3, targetFunc, 0.05)
