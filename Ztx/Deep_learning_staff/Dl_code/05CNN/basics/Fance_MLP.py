
from mxnet import nd
from mxnet import nn


class Fane_MLP(nn.Block):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)

        # 常数参数： 在训练过程中不会被迭代的参数值
        # 常数参数矩阵通常用来给模型引入一些固定的偏置
        self.rand_weight = self.params.get_constant(
            'rand_weight',nd.random.uniform(shape=(20,20))
        )
        
        self.dense = nn.Dense(20,activation='relu')

    def forward( self, X):

        # 1. 先使用dense层对输入进行一次计算
        X = self.dense(X)

        # 2. 加入常数参数矩阵的偏置后通过Relu激活函数
        X = nd.relu( nd.dot(X,self.rand_weight.data()) + 1) 

        # 3. 再次复用 self.dense 层
        X = self.dense(X)

        while X.norm().asscalar() > 1:
            X /= 2
        if X.norm.asscalar() < 0.8:
            X *= 10
        
        return X.sum()
        
