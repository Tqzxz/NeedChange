
" Model Selection and Evaluation"

""" 泛化误差
Generalization Error: The expected error of a model on unseen data.
Genearlization Error is always the goal that we want to minimize, and it is the evaluation of how well a model performs on new, unseen data.
"""

""" 模型选择
Usually, Different models have different ability to fit the training data, and we need to select the best model for our task.
The first step is by Using the training data to train some models, meanwhile we need to evaluate the performance of these models. Thus we 
could get a model with better performance on the training data.
However, the model with the best performance on the training data may not be the best model for unseen data.
To solve this problem, we need to use a validation set, which is a subset of the training data that is not used for training the model.

validation set is used for deciding a set of hyperparameters, such as the learning rate, the number of layers, and the number of neurons in each layer.

Finally, we can use the test set to evaluate the performance of the model with the best hyperparameters.
"""

"""
 Forawrd propagation /Backward propagation / Computation graph

 正向传播： 是指从在神经网络中， 输入层到输出层的过程，数据从输入层开始，经过各个隐藏层的计算，最终得到输出层的结果。

 举个例子： 假设输入X是一个D维特征的向量, 当输入向量进入神经网络后，可能会进行下面的计算过程:
   (1)Z =  W * X 计算各特征加权和.                                # W 是 K1 by D 的权重矩阵, X 是 D 维特征向量. 计算结果为 K1 by 1 的向量Z.
   (2)H = f(Z) 通过一些特定的激活函数，比如 ReLU 或 Sigmoid, 对 Z的每一个单元都进行非线性变换得到下一层的输入向量
   (3)O = W' * H 计算输出层的结果, 其中 W' 是 K2 by K1 的权重矩阵, H 是 K1 by 1 的向量. 计算结果为 K2 by 1 的向量O.

可以通过一个计算图来表示并存储输入向量的计算过程:

              
             |W1|                                       |W2|
              |                                          |
              V                                          V
    x ----->  * -------> Z ----> f(Z) ------> H -------> * -----> O


保留正向传播的计算图是为了在反向传播时能够使用链式法则来计算梯度。 在这之前我们需要先定义一个损失函数来衡量模型的输出与真实标签之间的差距，然后
而损失函数需要模型的前向传播结果O, 损失函数记作 L(O), 常见的损失函数有均方误差(MSE)和交叉熵损失(Cross-Entropy Loss)。


 反向传播： 是指在神经网络中， 计算每一个参数对损失函数的偏导数的过程。 而所有参数的偏导数组成了损失函数的梯度向量。
    这个梯度向量: 记作 G, 对于一个函数， 任意点的方向导数表示函数在该点的变化率。 方向导数和梯度有直接关系。
    方向导数 = G * u, 其中 u 是一个单位向量，表示方向。 由此可以看出方向导数的最大值为梯度向量的模长。
    方向导数表示这点的函数值沿着某个方向的变化率，梯度向量则表示函数在该点的最大变化率和方向。因为只有当单位向量和G方向相同时，方向导数最大值


# 通常在前向传播过程中，计算图会被构建出来，记录每一步的计算过程和中间结果。这个计算图可以用来在反向传播时计算梯度。
# 反向传播的计算过程是从输出层开始，逐层向前计算每个参数的梯度。这个过程可以通过链式法则来实现。

虽然反向传播理论上是梯度公式， 但是在实际计算中， 每一个参数的偏导数都是由具体的数据数据和参数来计算的。所以最后反向传播计算出的不过是一个
维度是所有参数的梯度向量值 G， 然后 优化器会根据不同方法来更新原有参数
"""
   