# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:09:17 2016

@author: weidner, matthew
"""

fib = 0

def fibonacci(n):
    series = [0,1]
    get_next(series,n)
    
def get_next(series,n):
    if len(series) != n:
        series.append(series[-2]+series[-1])
        get_next(series,n)
        
    else:
        print(series)


fibonacci(9)