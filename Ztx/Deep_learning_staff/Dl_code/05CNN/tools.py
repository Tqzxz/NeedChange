
from mxnet import autograd, nd
from mxnet.gluon import nn


def corr2d(X,K):
    '''
    X : 二维输入数据
    K : 二维卷积核数组
    '''

    height,width = K.shape
    Y = nd.zeros( (X.shape[0]-height + 1,X.shape[1]-width + 1) )

    for i in range(0,Y.shape[0]):
        for j in range(0,Y.shape[1]):
            Y[i,j] = (X[i:i+height,j:j+width]*K).sum()

    return Y

def corr2d_test():
    
    X = nd.array(
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    )

    K = nd.array(
        [
            [1,2],
            [3,4]
        ]
    )

    print(corr2d(X,K))

    return



if __name__ == "__main__":

    corr2d_test()

