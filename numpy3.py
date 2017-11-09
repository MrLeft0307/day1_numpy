#coding=utf-8
import numpy as np
'''
numpy的其他应用
'''
print (np.fft.fft(np.array([1,1,1,1,1,1,1,1])))#傅里叶变换

print (np.corrcoef([1,0,1],[0,2,1]))