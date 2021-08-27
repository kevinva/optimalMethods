# 一维搜索方法
from commons import fibonacci
import math

GOLDEN_CUT_POINT = 0.382
EPSILON_DEFAULT = 0.01


def goldenCutMethod(low: float, high: float, targetRangeLen: float, targetFunc):
    '''
    黄金分割法

    @param low 区间左端点
    @param high 区间右端点
    @param targetRangeLen 目标区间长度
    @param targetFunc 目标函数
    '''

    currentLen = abs(high - low)
    a = low
    b = high
    aVal = targetFunc(a)
    bVal = targetFunc(b)
    aTemp = low + GOLDEN_CUT_POINT * currentLen
    bTemp = low + (1 - GOLDEN_CUT_POINT) * currentLen
    while(currentLen > targetRangeLen):
        aVal = targetFunc(aTemp)
        bVal = targetFunc(bTemp)

        if aVal < bVal:
            b = bTemp
            currentLen = abs(a - b)   # 极小值在区间[a, bTemp]
            bTemp = aTemp
            aTemp = a + GOLDEN_CUT_POINT * currentLen
        else:
            a = aTemp
            currentLen = abs(a - b)   # 极小值在区间[aTemp, b]
            
            aTemp = bTemp
            bTemp = a + (1 - GOLDEN_CUT_POINT) * currentLen

        print('f(a) = {:.3f}, f(b) = {:.3f}, [{:.3f}, {:.3f}]'.format(aVal, bVal, a, b))
        
    return (a, b, aVal, bVal)
            


def fibonacciMethod(low: float, high: float, targetRangeLen: float, targetFunc, eps=EPSILON_DEFAULT):
    '''
    斐波那契法
    '''

    val = (1 + 2 * eps) / (targetRangeLen / abs(low - high))
    fibonacciList = list()
    n = 1
    f = fibonacci(n)
    fibonacciList.append(f)
    while f < val:
        n += 1
        f = fibonacci(n)
        fibonacciList.append(f)

    # 计算得迭代次数为n - 1

    a = low
    b = high
    rangeTag = 'none'
    for i in range(n - 1):
        currentLen = abs(a - b)
            
        p = 1 - fibonacciList[n - i - 2] / fibonacciList[n - i - 1]
        if i == n - 2: # 如果是最后一次迭代
            p -= eps

        if rangeTag == 'a':
            bTemp = a + (1 - p) * currentLen
        elif rangeTag == 'b':
            aTemp = a + p * currentLen
        else:
            aTemp = a + p * currentLen
            bTemp = a + (1 - p) * currentLen

        aVal = targetFunc(aTemp)
        bVal = targetFunc(bTemp)
        if aVal < bVal:
            b = bTemp
            bTemp = aTemp
            rangeTag = 'b'
        else:
            a = aTemp
            aTemp = bTemp
            rangeTag = 'a'

        print('f(a) = {:.3f}, f(b) = {:.3f}, [{:.3f}, {:.3f}]'.format(aVal, bVal, a, b))

    print('final range [{:.3f}, {:.3f}] is less than or equal to target range len: {} ? {}'.format(a, b, targetRangeLen, abs(a - b) <= targetRangeLen))
    return (a, b, aVal, bVal)
            
def newtonMethod(targetFunDiff, eps=EPSILON_DEFAULT, x0=0.5):
    '''
    牛顿迭代法
    '''

    x = x0
    while True:
        fVal, fDiff1 = targetFunDiff(x, 1)
        fVal, fDiff2 = targetFunDiff(x, 2)
        xNext = x - float(fDiff1) / float(fDiff2)
        # print('x next: {}, fDiff1: {}, fDiff2: {}'.format(xNext, fDiff1, fDiff2))
        if abs(xNext - x) < eps:
            finalDiff1 = targetFunDiff(xNext, 1)[1]
            finalDiff2 = targetFunDiff(xNext, 2)[1]
            # 检查是否满足极小点的一阶必要条件
            print('first order derivative: {}, second order derivative: {}'.format(finalDiff1, finalDiff2))
            break
        else:
            x = xNext
        print('f(x) = {:.3f}, x = {:.3f}'.format(fVal, x))
    return x


def cuttingLineMethod(targetFuncDiff, x0_1, x0_2, eps=EPSILON_DEFAULT):
    '''
    割线法
    '''

    x1 = x0_1
    x2 = x0_2
    while True:
        fVal1, fDiff1 = targetFuncDiff(x1, 1)
        fVal2, fDiff2 = targetFuncDiff(x2, 1)
        
        xNext = float(fDiff2 * x1 - fDiff1 * x2) / (fDiff2 - fDiff1)
        print('xk = {}'.format(xNext))

        finalVal, finalDiffFirst = targetFuncDiff(xNext, 1)
        finalVal, finalDiffSecond = targetFuncDiff(xNext, 2)
        print('f(xk) = {}, first order derivative: {}, second order derivative: {}'.format(finalVal, finalDiffFirst, finalDiffSecond))

        if abs(finalDiffFirst) < eps:
            break
        else:
            x1 = x2
            x2 = xNext
    return x2


def findMiniPointBoundaryForFunction(targetFunc):
    '''
    划界法寻找极小点所在区间
    '''

    x1 = 0
    x2 = x1 + EPSILON_DEFAULT
    x3 = x2 + 2 * EPSILON_DEFAULT
    n = 1
    while True:
        f1 = targetFunc(x1)
        f2 = targetFunc(x2)
        f3 = targetFunc(x3)
        if (f1 > f2) and (f3 > f2):
            break
        elif (f1 > f2) and (f2 > f3):
            x3 += abs(x3 - x2) * (n + 1)
        n += 1

    print('result range: [{}, {}]'.format(x1, x3))
    return (x1, x3)