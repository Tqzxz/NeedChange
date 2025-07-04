
'''
   LeNet是一个很早的卷积神经网络， 也是最先采用卷积这一操作来建模型处理图像数据的（主要是手写数字识别）， 但是从深度学习角度来说， 这个
   模型并不复杂，也不深，但是在那时模型效果确实非常好。

   但是在之后的时间，LeNet也是又被传统机器学习算法例如支持向量机超越。问题出现在LeNet在更大的真实数据集上表现并不好。

   AlexNet和 LeNet的架构相似，但是参数量要比LeNet大的多
'''

import d2lzh as d2l
import mxnet as mx
from mxnet import gluon, init, nd
from mxnet.gluon import data as gdata, nn
from mxnet.gluon import loss as gloss
import os
import time
import sys

class AlexNet(nn.Sequential):
    
    def __init__( self,):

        super().__init__()

        self.add(
            nn.Conv2D(channels=96, kernel_size=11,strides=4,activation='relu'),
            nn.MaxPool2D(pool_size=3,strides=2),
            nn.Conv2D(channels=256,kernel_size=5,padding=2,activation='relu'),
            nn.MaxPool2D(pool_size=3,strides=2),
            nn.Conv2D(channels=384, kernel_size=3,padding=1,activation='relu'),
            nn.Conv2D(channels=384, kernel_size=3,padding=1,activation='relu'),
            nn.Conv2D(channels=256, kernel_size=3,padding=1,activation='relu'),
            nn.MaxPool2D(pool_size=3,strides=2),
            nn.Dense(4096,activation='relu'),nn.Dropout(0.5),
            nn.Dense(4096,activation='relu'),nn.Dropout(0.5),
            nn.Dense(10)
        )

        self.initialize(force_reinit=True, init=init.Xavier())

    def test(self,):
        for layer in self:
            print(layer.name)

if __name__ == "__main__":

    net = AlexNet()
    net.test()