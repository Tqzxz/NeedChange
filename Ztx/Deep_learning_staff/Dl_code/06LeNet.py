
import d2lzh as d2l  
import mxnet as mx 
from mxnet import autograd, nd, gluon, init
from mxnet.gluon import loss as gloss, nn
from mxnet.gluon import data as gdata
import time
import sys

class LeNet(nn.Sequential):
    
    def __init__( self, ctx):

        super().__init__()

        self.add(
            nn.Conv2D(channels=6, kernel_size=5, activation='sigmoid'),
            nn.MaxPool2D(pool_size=2,strides=2),
            nn.Conv2D(channels=16,kernel_size=5,activation='sigmoid'),
            nn.MaxPool2D(pool_size=2,strides=2),
            nn.Dense(120,activation='relu'),
            nn.Dense(84,activation='relu'),
            nn.Dense(10)
        )

        self.initialize(force_reinit=True,ctx=ctx, init=init.Xavier())

    def test(self,):
        for layer in self:
            print(layer.name)

class model:

    def __init__(self, num_epochs, batch_size, learning_rate):

        self.ctx        = self.try_gpu()
        self.net        = LeNet(self.ctx)
        self.train_iter, self.test_iter = self.generate_iter(batch_size)
        self.trainer    = gluon.Trainer(self.net.collect_params(), 'adam', {'learning_rate':learning_rate})

        self.train( self.net, self.train_iter, self.test_iter, batch_size, self.trainer, self.ctx, num_epochs)

    def try_gpu( self, ):
        
        try:
            ctx = mx.gpu()
            _   = nd.zeros((1,), ctx =ctx)

        except mx.base.MXNetError:
            ctx = mx.cpu()

        return ctx

    def generate_iter( self,batch_size ):

        transformer = gdata.vision.transforms.ToTensor()
        
        if sys.platform.startswith('win'):
            num_workers = 0
        else:
            num_workers = 4

        mnist_train = gdata.vision.FashionMNIST(train=True)
        mnist_test  = gdata.vision.FashionMNIST(train=False)
        train_iter = gdata.DataLoader(mnist_train.transform_first(transformer), batch_size,shuffle=True,num_workers=num_workers)
        test_iter  = gdata.DataLoader(mnist_test.transform_first(transformer), batch_size,shuffle=True,num_workers=num_workers)
        
        return train_iter,test_iter

    def evaluate_acc( self, data_iter, net, ctx):
        acc_sum, n = nd.array([0], ctx=ctx), 0
        for X, y in data_iter:
            X,y = X.as_in_context(ctx), y.as_in_context(ctx).astype('float32')
            acc_sum += ( net(X).argmax(axis=1) == y ).sum()
            n+= y.size 
        return acc_sum.asscalar() / n

    def train( self, net, train_iter, test_iter, batch_size, trainer, ctx, num_epochs):
        
        print(f" Training is on {ctx}")

        loss = gloss.SoftmaxCrossEntropyLoss()

        for epoch in range(num_epochs):

            train_l_sum, train_cc_sum, n, start = 0.0, 0.0, 0, time.time()

            for X, y in train_iter:
                X, y = X.as_in_context(ctx), y.as_in_context(ctx)
                with autograd.record():
                    y_hat = net(X)
                    l     = loss(y_hat, y).sum()
                l.backward()
                trainer.step(batch_size)
                y = y.astype('float32')
                train_l_sum += l.asscalar()
                train_cc_sum += (y_hat.argmax(axis=1) == y).sum().asscalar()
                n+=y.size
                
            test_acc = self.evaluate_acc(test_iter,net, ctx)
            
            print('epoch %d, loss %.4f, train_acc %.3f, test_acc %.3f, ' 'time %.1f sec' % (epoch + 1, train_l_sum/n, train_cc_sum /n , test_acc, time.time() - start))

if __name__ == "__main__":

    num_epochs = 50
    batch_size = 256
    learning_rate = 0.01

    model = model( num_epochs, batch_size, learning_rate )

    


    
        
    