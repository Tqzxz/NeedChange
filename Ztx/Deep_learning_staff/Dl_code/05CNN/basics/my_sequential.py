
from mxnet import nd
from mxnet.gluon import nn 


class MySequential(nn.Block):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def add(self, block):
        
        # nn.Block 是一个通用的部件，block的子类可以是一个层，或者是一个模型
        # 这里参数的block表示是一个block的子类，block有name的属性来标识该block
        self._children[block.name] = block
        # 可以看出shel._children应该是一个字典，key是block_name, val是block实例

    def forward( self, X):

        for block_instance in self._children.values():
            X = block(X)
        
        return X
