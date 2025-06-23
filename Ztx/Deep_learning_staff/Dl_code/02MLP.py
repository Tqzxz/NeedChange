from mxnet import nd
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn
import d2lzh as d2l

class MLP:

    def __init__( self,):

        self.net = nn.Sequential()
        self.net.add(nn.Dense(256),nn.LeakyReLU(0.01),nn.Dense(128),nn.LeakyReLU(0.01),nn.Dense(128),nn.LeakyReLU(0.01),nn.Dense(64),nn.LeakyReLU(0.01),nn.Dense(10))
        self.net.initialize(init.Xavier())

    def train(self, batch_size=32, num_epochs=20, lr=0.001):

        train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

        loss = gloss.SoftmaxCrossEntropyLoss()

        trainer = gluon.Trainer(self.net.collect_params(), 'adam', {'learning_rate': lr})

        d2l.train_ch3(self.net, train_iter, test_iter, loss, num_epochs ,batch_size ,None, None, trainer)

        
if __name__ == '__main__':

    mlp = MLP()
    mlp.train()
    print("Training complete.")
