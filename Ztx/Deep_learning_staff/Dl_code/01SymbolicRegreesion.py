'''
1.  Intro

  用 using SymbolicRegression     符号回归？ 是啥
     using MJL


  X = 2randn(1000,5)
  y = @ . 2*cos( X[:,4] ) + X[:, 1]^2 -2

  model = SRRegressor(
      binary_operations=[*.-.+./]     //允许模型使用/预测范围的二元操作符
      unary_opearators =[cos]         //允许模式使用的一元操作符
      niteration       = 30           //迭代次数
  )

///////////////////////////////////////////////////////////////////////////////

2. 自定义操作符

  X = 2randn(1000,5)
  y = @. 1/X[:,1]

  my_inv(x) = 1/x

  model = SRRegreesor(
      binary_operators=[+,*],
      unary_operators=[my_inv],
  )

  match = machine(model,X,y)
  fit!(match)
  r = report(match)
  println(r.equations[r.best_idx])

///////////////////////////////////////////////////////////////////////////////

SymbolicRegression符号回归API(Julia 版本)


MJL interface ( SymbolicRegression.MJLInterfaceModule.SRRegressor )

1. 导入模型
    SiRegreesor = @load SiRegressor pkg=SymbolicRegression
    model       = SiRegreesor()
    model       = SiRegreesor(
          //带参数创建模型实例
    )
2. 数据绑定和训练

    mach  = machine(model, X, y)
    mach  = machine(model, X, y, w) //带权重的绑定数据

    fit!(mach)  //训练模型
////////////////////////////////////////////////////////////////////////////////////////

    符号回归是一种传统机器学习方式， 用来拟合输入数据中潜在存在的非线性关系

    1. 遗传算法
    核心原理是遗传编程.Genetic Programming, 大概过程是最先随机地生成一个计算公式，并根据预测效果修改计算公式，不断地迭代后，得到一个损失较小的最终版
    遗传算法遵循生物的进化过程： (1)过度繁殖 (2)遗传变异 (3)生存斗争 (4)适者生存
              选择：
              交叉：
              变异：
    大体过程： 
    a. 随机初始化一组(多个)解,这些解被称为染色体个体，多个个体组成在一起为种群
    b. 染色体个体编码过程
    c. 适应度评估，建立一个适应度评估函数来对每一个染色体的适应度（类似损失函数）
    d. 选择/(杀死)
    e. 交叉繁殖
    f. 子代变异
    
    步骤详解：
    b. 编码
      把实际问题转换为遗传算法接收的形式：比如二进制编码, 浮点编码, 符号编码

////////////////////////////////////////////////////////////
1. using MJL
2. 导入模型 SRRegressor = @load SRRegressor pkg=SymbolicRegression
3. 模型初始化的一些超参数
model = SRRegressor(
    binary_operators 允许模型使用的二元操作符
    unary_operators  允许模型使用的一元操作符
    population_size  每一轮遗传算法染色体数量
    niterations      迭代轮数
    parsimony        计算式复杂度惩罚系数 
    batching + batch_size 批处理
    earlY_STOP_condition  早停
     .
     .
     . 
    )
 4. 训练模型 mach = machine(model, X, y)
 5. y_pred = predict(mach,Xnew)
 6. best_formula = report(mach).bset_selection

//需要注意 log, div运算需要处理负值和0值的情况
'''
