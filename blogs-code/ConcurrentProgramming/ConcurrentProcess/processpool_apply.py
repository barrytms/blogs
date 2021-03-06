#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：Lyon
from multiprocessing import Pool
import os
import time
def run(n):
    print("%s run..." % os.getpid())
    time.sleep(2)
    return n**2

if __name__ == '__main__':
    pool = Pool(3)
    res_list = []
    for i in range(10):
        res = pool.apply(run, args=(i,))
        res_list.append(res)
    print(res_list)