
from mxnet import nd
from mxnet.gluon import nn
import d2lzh as d2l 
from tools import corr2d


def corr2d_multi_in( X, K):

    return nd.add_n(*[d2l.corr2d(x,k) for x,k in zip(X,K)])

def corr2d_multi_out_1x1(X, K):

    c_i, h, w = X.shape
    c_o  = K.shape[0]
    X.reshape( (c_i, h * w))
    K.reshape( (c_o, c_i))
    


if __name__ == "__main__":

    X = nd.array(
        [
            [
                [0,1,2],
                [3,4,5],
                [6,7,8]
            ],
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
        ]
    )

    K = nd.array(
        [
            [
                [0,1],
                [2,3]
            ],
            [
                [1,2],
                [3,4]
            ]
        ]
    )

    print(corr2d_multi_in(X,K))