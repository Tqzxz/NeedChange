Key things !!!!
1. Control method is the most important techique in this project, very likely related to control theory PID, LQR, MPC, Nureal Network based(Deep learning) , Reinforcement learning


Current Goal Minimium Functionality:


Learning Staff:
1. Driving Step Motors with proper driving board ( language: C/C++, or Python )
2. Bottom PID controll


  1. Robot base that could move( --- ):
     
     轮足： 确定是用轮足，但是具体怎么整还没确定， 用一个两个还是几个， 放在什么样的位置 （ 或者考虑吧换一种轮子的类型， 麦克纳木轮， 但感觉有点花）
     电机： 底座的驱动电机肯定力矩要大一点， 转速不需要太快。 底座电机选型 ( 直流电机应该可以？， 步进电机感觉更适合上身的控制， 并且需要有车轮编码器)
     减震： 需不需要呢， 感觉不是那么需要， 后面可以尝试加一下
     控制板： 底座MCU可以用 esp32， 或者更好一点的， 但esp32应按可以？（ esp32没有系统， 就可以运行一些写好的程序， 所以可能需要另一个带系统的板子来控制esp32， 比如树莓派....）
     材料： 刚开始可以用3D打印， 后面可以考虑要不要换成金属的（ 金属的会好一点， 因为重心会偏低， 更稳一点）
     确定控制方式（上半身同步控制， 手掌手臂头部腰部， 下半身脚踩机关控制机器人底座电机）
     (1). 确定底座(外形)，电机，控制板
    （2). 电机、底座模型打印出来测试测试一些功能（ 直线， 斜线， 直角 ）
     (3). （2）加入PID controller 再测试测试

  2. Create an Third Party Interface to capture Time-to-Time Robot information( HP, velocity, location..)
      暂时先不管



Basic Control path:
//
         |   控制信号输入 |   
                         +---------+----------+
                                   ↓
                        +----------+-----------+
                        |        滤波器        |
                        |      滤除高频抖动     | ---------------- Filters.. 
                        |                      |
                        +----------+----------+
                                   ↓
                        +----------+-----------+
                        |        协调器         |
  robot perception ---->|  判断是否可执行动作    | --------------- Top controller （ Model-Based ）
                        |   生成优化控制信号     |
                        +----------------------+
                                   ↓
                        +----------+------------+
  robot perception ---->|     姿态控制（微调）    | --------------- Base Controller ( PID )
                        |   仅在动作执行中小幅修正 |
                        +---------+-------------+
                                 ↓
                            +----+----+
                            | 执行器组 |   ------------------------ Motors
                            +---------+




