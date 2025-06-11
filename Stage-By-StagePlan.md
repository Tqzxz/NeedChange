![image](https://github.com/user-attachments/assets/8b102942-117e-4e41-b47a-cb56cbcac549)
# general description：
  控制方式： 玩家同步控制机器人运动包括（移动，使用武器）//算法优化动作的执行 通过一些外部传感器采集用户的运动，传递给机器人。  （上半身可以同步控制，下半身可以就是踩左右脚油门等）
  玩法    ： 多人线下竞技( 类似红蓝方对抗， 射击类)
  机制    ： 
    1.属性成长（软件限制硬件的最大功率等等）， 比如随着成长， 软件逐渐对电机的最大功率提高， 装备也会提高属性
    2.武器机制：机器人可以装备一些外部武器防具辅助道具等， 不同组合触发不同效果， 可以使用特殊技能。 射击武器只能使用低动能子弹比如BB弹，水弹等等， 可以给子弹上标签在被攻击的时候可以区分子弹来源
    3.虚拟HP  ：对每个机器人初始化虚拟血条、蓝条、电量、能量条等等
    4.负面效果： 机器人身上可以安装多个传感器，检测是否被攻击到  电量/血量为0，则被外部工作人员或者其他方式送回复活点
    5.moba迷雾机制：没有全部地图视野， 视野来源是从机器人头部的摄像头传递回来， 装备属性/属性成长也包括视野
    6 地图  ： 非平面地图， 有虚拟回复血量能量的机制， 
    7.技能  ： 不同机器人初始属性不同，硬件配置不同， 功能性不同。 可使用专属技能，但需要属性达到一定值， 属性越高， 攻击/技能造成的血量损失越高
    8.胜利机制：可以采用moba推塔的方式，或者其他别的 再想想
    ..其他的再想想 

Key things
1. Control method is the most important techique in this project, very likely related to control theory PID, LQR, MPC, Nureal Network based(Deep learning) , Reinforcement learning


Current Goal : Minimium Functionality

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

    赵清玉：
    关于外形：我们真的要做人形机器人吗，关于人形机器人轮子放在脚上有点僵。
    我的想法是做轮子是履带的那种，这样不管是控制还是其他的都好些
    ![image](https://github.com/user-attachments/assets/eb7cfe23-a819-423b-84d9-ec87b37f1165)

    
    

  3. Create an Third Party Interface to capture Time-to-Time Robot information( HP, velocity, location..)
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




