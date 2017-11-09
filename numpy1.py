#coding=utf-8
import numpy as np
'''
第一天，尝试使用numpy
'''

def startMain():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    print (np_lst.shape)  #打印 两行三列
    print (np_lst.ndim)
    print (np_lst.dtype)
    print (np_lst.size)
    print (np_lst.itemsize)

    #其他方法
    #创建矩阵
    print (np.zeros([2,4]))
    print (np.ones([3,3]))
    #打印随机数(0-1之间)
    print ("Rand:")
    print (np.random.rand(2,4))
    print (np.random.rand())

    #打印三个1到10之间的整数
    print (np.random.randint(1, 10, 3))

    #打印标准正太分布的数字, 还可以生成其他分布的
    print (np.random.randn(2, 3))

    #打印给定数据其中的一个数字
    lst = [1, 3, 5, 9, 10]
    print (np.random.choice(lst))

    #生成1到11，不包括11，并且可以将其变成矩阵
    print(np.arange(1, 11).reshape([2, 5]))
    lst = np.arange(1, 11).reshape([2, 5])
    print (np.exp(lst))
    print (np.exp2(lst))
    print (np.sqrt(lst))
    print (np.log(lst))



    lst1 = np.array([10, 20, 30, 70])
    lst2 = np.array([15, 20, 30, 60])

    print "Cancatenate"
    print (np.concatenate((lst1, lst2,), axis=0))
    print (np.vstack((lst1, lst2)))#连接起来,但是是两行
    print (np.hstack((lst1, lst2)))#连接起来
    print (np.split(lst1, 2))#分开
    print (lst1.sum(axis=0))
    print (lst1.sum(axis=1))
if __name__=="__main__":
    startMain()