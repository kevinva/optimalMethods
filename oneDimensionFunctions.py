# 一维搜索方法
from commons import fibonacci
import math

GOLDEN_CUT_POINT = 0.382
EPSILON_DEFAULT = 0.01


def goldenCutWithRange(low: float, high: float, targetRangeLen: float, targetFunc):
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
            


def fibonacciWithRange(low: float, high: float, targetRangeLen: float, targetFunc, eps=EPSILON_DEFAULT):
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
            
    # print(fibonacciList)
