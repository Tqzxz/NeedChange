

'''
    批量归一化 

    为什么需要批量归一化：
        因为在更新网络参数的时候， 即使很小的参数更新，但会对输出造成非常大的影响，可能输出会天差地别
        为了避免这种不稳定的输出， 得到更稳定/逐渐优化的输出 10和11讲了两种方式
        
    对什么东西归一化：
        对神经网络中的某些layer ouput归一化处理, 是对输出进行归一化处理

'''

'''
    1. 对全链接层MLP 批量归一化

    批量归一化 上一层的batch output 记作 x, 按照特征维度计算均值,方差，然后标准化
    x ->(normalize) -> y -> hyperarameter(a,b) ay + b -> batchNorm output
                                    |
                                    |
                                  (a,b)

    Output = a * ((Batch_X - Batch_mean) / Batch_Sigma) + b

    然后Ouput作为激活函数的输入

    训练过程中，如果 a == Batch_mean , b == Batch_Sigma, 那么等于 Batch Normalization 啥也没干

    加入 BatchNorm 后，理论上可以去掉全连接层的 bias(常量偏移项), 
    因为 BatchNorm 本身有可学习的平移(beta)和缩放(gamma)参数,能实现同样的效果。
    并且全链接层的常数偏置会在计算均值时会被包含进去，然后在标准化的时候会被减掉，所以可以去掉，没有影响，还可以
    减少不必要的计算和存储


    2. 对卷积层Cov   批量归一化


'''

