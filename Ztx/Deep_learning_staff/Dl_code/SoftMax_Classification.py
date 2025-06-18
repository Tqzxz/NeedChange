from mxnet import autograd, nd
import d2lzh as d2l

class softmax_model:

    def __init__( self, ):

        self.train_data = None
        self.test_data  = None

    def data_load( self, batch_size):
        
        train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)
        
    def softmax_layer( self, ):

        num_inputs  = 784
        num_outputs = 10

        self.w = nd.random.normal(scale=0.01,shape=(num_inputs, num_outputs))
        self.b = nd.zeros(num_outputs)

        w.attach_grad()
        b.attach_grad()

    def softmax( self, X):
        
        X_exp     = X.exp()
        partition = X_exp.sum(axis=1,keepdims=True)
        return X_exp / partition

    def net( self, X):

        return self.softmax( nd.dot(X.reshape(-1,num_inputs),self.w) + self.b )


    def ce_loss( self, y, y_hat):

        return -nd.pick(y_hat,y).log()





if __name__ == "__main__":

    model = softmax_model()
    model.test()
    