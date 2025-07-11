
# 2025.06.11 Updated

赵清玉：
1. 关于外形：我们真的要做人形机器人吗，关于人形机器人轮子放在脚上有点僵。我的想法是做轮子是履带的那种，这样不管是控制还是其他的都好些：

<p align="center">
  <img src="https://github.com/user-attachments/assets/eb7cfe23-a819-423b-84d9-ec87b37f1165" alt="image" />
</p>

朱天栖：


# 2025.06.13 Updated

  前两天大概确定了干什么， 写在了general_description里面。 然后开始搞第一步， 把硬件什么的给选了。
  General_description里面就写项目的信息
  Developement_Info里面记录一些技术细节

ztx: 一起商量了一下，应该选什么样的主控板，主要是在价格/性能上有点取舍，更新了 Development_Info 把底座驱动的大概通信结构画了出来。
zqy:

# 2025.06.18 Updated

ztx:

  板子刚到了两天，还有摄像头。 然后这两天把 开发工具还有环境配置了一下， 但是esp32源代码有点复杂，看不懂。还有freeros
  等晚上回去先运行一下blink点灯的例子看看情况。

zqy:

# 2025.07.01 Updated

ztx: 

  这几天没有怎么看ESP32，小摆

# 2025 07.11 Updated

ztx:

  学了ESP32的MCPWM大概的控制方式， 如果直接连电机，一个电机驱动需要5根线(GND,Vcc,encoderA,encoderB,DIR,BRAKE,PWM), 但GND,Vcc,应该可以公用，所以两个电机应该需要10个GPIO和一个GND
  准备看看怎么用电脑和ESP32通信， 还挺麻烦的。P4 module板子没有直接用无线通信的方法，但是板子上有一个esp32 C6无线模块可以。 所以
  得用 esp-host 主从机的方式，这个相对还不算太复杂， 就是配置一下硬件，最后还是可以在app_mian()里面调用一些API来通信，
  但是复杂的是 一般无线通信都需要有一个服务器，GATT比较常用， 但是有点复杂

  





