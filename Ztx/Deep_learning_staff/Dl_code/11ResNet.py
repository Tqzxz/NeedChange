

'''
    残差网的特点在于它使用了残差连接(skip connections),
    
    跳跃连接的效果很好, 原因在于
    (1) 从实验结果上看,ResNet解决了堆叠层数导致训练效果下降的问题, 
    深度网络的梯度消失问题, 通过残差连接可以让梯度更容易地传递到前面的层。
'''

import d2lzh as d2l 
from mxnet import gluon, init, nd
from mxnet.gluon import nn 


class Residual(nn.Block):

    def __init__( self, num_channels, use_1x1conv=False, strides=1, **kwargs):
    
        super().__init__()

        self.input1_conv = nn.Conv2D(num_channels, kernel_size=3, strides=strides, padding=1)
        self.input2_conv = nn.Conv2D(num_channels, kernel_size=3, strides=1, padding=1)

        if use_1x1conv:
            self.conv3 = nn.Conv2D(num_channels, kernel_size=1, strides=strides)
        else:
            self.conv3 = None
        
        self.bn1 = nn.BatchNorm()
        self.bn2 = nn.BatchNorm()

    def forward( self, X):

        Y = nd.relu(self.bn1(self.input1_conv(X)))
        Y = self.bn2(self.input2_conv(Y))
        if self.conv3:
            X = self.conv3(X)
        return nd.relu(Y + X)
    

if __name__ == '__main__':
    net = Residual(3, use_1x1conv=True, strides=2)
    net.initialize(init=init.Xavier())
    X = nd.random.uniform(shape=(4, 3, 6, 6))
    Y = net(X)
    print(Y.shape)  # (4, 3, 3, 3)

    


