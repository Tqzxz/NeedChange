
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

'''
