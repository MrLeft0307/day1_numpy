#coding=utf-8
import numpy as np
'''
python 矩阵操作与线性方程
'''
from numpy.linalg import*
print (np.eye(3))
lst = ([[1, 2],
        [3, 4]])
#矩阵的逆
print(inv(lst))

#矩阵的行列式

print(det(lst))

#矩阵的转置

print (np.transpose(lst))

#特征值与特征向量
print (eig(lst))

#结二元一次方程组
y = np.array([[5],
              [7]])
print (solve(lst,y))


