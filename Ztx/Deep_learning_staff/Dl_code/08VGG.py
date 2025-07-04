
'''
    VGG也是一个基于卷积层的网络, 特点是重复使用简单的基础块搭建复杂网络
'''

import d2lzh as d2l
import mxnet as mx
from mxnet import gluon, init, nd
from mxnet.gluon import data as gdata, nn
from mxnet.gluon import loss as gloss
import os
import time
import sys

class VGG(nn.Sequential):
    
    def __init__( self, conv_arch):

        super().__init__()

        for (num_convs, num_channels) in conv_arch:
            
            self.add( self.vgg_block(num_convs, num_channels) )
        
        self.add(
            nn.Dense(4096,activation='relu'),nn.Dropout(0.5),
            nn.Dense(4096,activation='relu'),nn.Dropout(0.5),
            nn.Dense(10)
        )

        self.initialize(force_reinit=True, init=init.Xavier())

    def vgg_block(self, num_convs, num_channels):
        
        block = nn.Sequential()
        for _ in range(num_convs):
            block.add(nn.Conv2D(channels=num_channels,kernel_size=3,padding=1,activation='relu'))
        
        block.add(nn.MaxPool2D(pool_size=2,strides=2))

        return block

    def test(self,):
        for layer in self:
            print(layer.name)

if __name__ == "__main__":

    conv_arch = [(3,3)]
    net = VGG(conv_arch)
    net.test()