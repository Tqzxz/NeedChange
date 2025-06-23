
from mxnet import autograd, nd, init
from mxnet import gluon
from mxnet.gluon import data as gdata
from mxnet.gluon import loss as gloss
from mxnet.gluon import nn
import random
from time import time
import d2lzh
# from IPython import display

class ML_pipeline:

    def __init__( self, ):

        self.data_set = None 
        self.labels   = None 

    def linear_regression_generate_data_set( self, ):
        
        feature_nm = 2
        data_nm    = 1000

        default_w  = [2, -3.4]
        default_b  = 4.2

        ## random_data is a 1000 by 2 tensors
        self.data_set = nd.random.normal(scale=1, shape=(data_nm,feature_nm))

        self.labels  = default_w[0] * self.data_set[:,0] + default_w[1] * self.data_set[:,1] + default_b

        self.labels  += nd.random.normal(scale=0.01, shape=(self.labels.shape))

        return 
    
    def run( self, ):

        self.linear_regression_generate_data_set()

        batch_size = 10
        data_set   = gdata.ArrayDataset( self.data_set, self.labels )
        data_iter  = gdata.DataLoader(data_set, batch_size, shuffle=True)

        # w = nd.random.normal(scale=0.01, shape=(len(self.data_set), 1))
        # b = nd.zeros(shape=(1,))
        net = nn.Sequential()

        net.add(nn.Dense(1))

        net.initialize(init.Normal(sigma=0.01))

        loss = gloss.L2Loss()
        
        trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate':0.03})

        num_epoch = 3

        for epoch in range(1, num_epoch+1):
            for x, y in data_iter:
                with autograd.record():
                    l = loss(net(x),y)
                l.backward()
                trainer.step(batch_size)
            l = loss(net(self.data_set), self.labels )
            print(f'epoch {epoch}, loss:{l.mean().asnumpy()}')



if __name__ == "__main__":

    ml_test = ML_pipeline()
    ml_test.run()
