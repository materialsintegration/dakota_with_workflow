#!python3.6
# -*- coding: utf-8 -*-

'''
Rosenbrock評価関数

'''
import sys

def rosenbrock_for_bayes(x, y):
    '''
    Rosenbrock関数、Bayes推定用
    '''

    return -1.0 * (100 * (y - x ** 2) ** 2 + ( 1 - x) ** 2)

def rosenbrock_for_conmin(x, y):
    '''
    Rosenbrock関数、最急降下法用
    '''

    return 100 * (y - x ** 2) ** 2 + ( 1 - x) ** 2

def main():
    '''
    開始点
    '''

    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    except:
        print("Usage")
        print("python %s x y"%sys.argv[0])
        print("    x: -5.0 < x < 5.0")
        print("    y: -5.0 < y < 5.0")
        sys.exit(1)

    ret = rosenbrock_for_conmin(x, y)
    print(ret)

if __name__ == '__main__':
    main()


