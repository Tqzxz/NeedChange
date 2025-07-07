
import d2lzh as d2l 
import mxnet as mx
from mxnet import gluon, init, nd
from mxnet.gluon import data as gdata
from mxnet.gluon import nn 
import sys

class Dense_Block(nn.Block):

    def __init__(self, num_convs, num_channels):

        super().__init__()

        self.net = nn.Sequential()
        
        for _ in range(num_convs):
            self.net.add(Conv2D(num_channels))

    def forward( self, X):

        for blk in self.net:
            Y = blk(X)
            X = nd.concat(X,Y, dim=1)

        return X

def transition(num_channels):

    blk = nn.Sequential()
    blk.add(
        nn.BatchNorm(),
        nn.Activation('relu'),
        nn.Conv2D(num_channels, kernel_size=1),
        nn.AvgPool2D(pool_size=2, strides=2)
    )
    
    return blk

def Conv2D(num_channels):

    blk = nn.Sequential()
    blk.add(
        nn.BatchNorm(),
        nn.Activation('relu'),
        nn.Conv2D(num_channels, kernel_size=3,padding=1)
    )

    return blk

class DenseNet(nn.Block):

    def __init__(self):
        
        super().__init__()

        self.net = nn.Sequential()
        self.net.add(
            nn.Conv2D(64, kernel_size=7, strides=2, padding=3),
            nn.BatchNorm(),
            nn.Activation('relu'),
            nn.MaxPool2D(pool_size=3, strides=2, padding=1)
        )

        inout_channels = 64
        num_Dense_blk  = 4
        num_convs      = 4
        num_channels   = 32

        for i in range(num_Dense_blk):

            self.net.add(
                Dense_Block(num_convs, num_channels)
            )
            inout_channels += num_convs * num_channels

            if i != num_Dense_blk - 1:
                self.net.add(
                    transition(inout_channels // 2)
                )
                inout_channels = inout_channels // 2

        self.net.add(
            nn.BatchNorm(),
            nn.Activation('relu'),
            nn.GlobalAvgPool2D(),
            nn.Dense(10)  # Assuming 10 classes for classification
        )

    def forward( self, X):

        return self.net(X)

def try_gpu():
    
    try:
        ctx = mx.gpu()
        _   = nd.zeros((1,), ctx =ctx)

    except mx.base.MXNetError:
        ctx = mx.cpu()

    return ctx

def generate_iter(batch_size ):

        transformer = gdata.vision.transforms.Compose([
        gdata.vision.transforms.Resize(96),   
        gdata.vision.transforms.ToTensor()   
    ])
        
        # if sys.platform.startswith('win'):
        #     num_workers = 0
        # else:
        #     num_workers = 4
        num_workers = 0
        mnist_train = gdata.vision.FashionMNIST(train=True)
        mnist_test  = gdata.vision.FashionMNIST(train=False)
        train_iter = gdata.DataLoader(mnist_train.transform_first(transformer), batch_size,shuffle=True,num_workers=num_workers)
        test_iter  = gdata.DataLoader(mnist_test.transform_first(transformer), batch_size,shuffle=True,num_workers=num_workers)
        
        return train_iter,test_iter

def train(net,batch_size, ctx, num_epochs):

    net.initialize(ctx=ctx, init=init.Xavier())
    trainer = gluon.Trainer(net.collect_params(), 'adam', {'learning_rate': 0.1})
    train_iter, test_iter    = generate_iter(batch_size)
    d2l.train_ch5(net, train_iter, test_iter, batch_size, trainer, ctx, num_epochs)


if __name__  == '__main__':

    net = DenseNet()

    ctx = try_gpu()
    
    batch_size = 256
    num_epochs = 10

    train(net, batch_size, ctx, num_epochs)