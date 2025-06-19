from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn
import d2lzh as d2l

class softmax_model:

    def __init__( self, ):

        self.net = nn.Sequential()
        self.net.add(nn.Dense(10))
        self.net.initialize(init.Normal(sigma=0.01))

    def test( self, num_epoch=10, batch_size=128):

        train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

        loss = gloss.SoftmaxCrossEntropyLoss()

        trainer = gluon.Trainer(self.net.collect_params(), 'sgd', {'learning_rate': 0.015})

        d2l.train_ch3(self.net, train_iter, test_iter, loss, num_epoch, batch_size, None, None, trainer)
        

if __name__ == "__main__":

    model = softmax_model()
    model.test()
    