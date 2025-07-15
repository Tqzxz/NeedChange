

# ALL_func_test project <br>

## 1. Intro and explain <br>

__The Aim for this is to explain how some of ESP32 modules works and show the correct way of using their ESP APIs(SPI,MCPWM) and how build project and run project on a ESP32 board__<br>   
__--2025.07.09__<br>

## 2. 准备工作
1. 需要有一个Linux系统/虚拟机环境, 第一步需要先在终端输入一些下载工具的指令<br>
 ``` linux
    sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```  
下载必要工具比如 python3, cmake, venv 等等， 需要注意 Cmake需要3.16及以上的版本，老版本Linux系统运行指令可能下载的是老版本Cmake, 需要先升级系统或者直接下载Cmake3, 有些工具比如python3大概率Linux系统是自带，有些工具有就可以不用下，怎么系统升级，查看是否下载了某些工具这些指令上网一搜就有<br>

2. 下载好了这些工具之后，就可以来下载ESP32官方提供的开发工具 ESP-IDF 了，这个工具里面有非常多的内容， 其中包括ESP32底层的源代码，编译你项目的脚本程序，等等。这个项目就是从ESP32底层源码向上抽象了一层，将一些可以合并的函数合并成一个功能。<br>
<br>
在github找到 ESP32 IDF 仓库https://github.com/espressif/esp-idf  之后，把这个项目复制到本地，并且一定要记住存放这个项目的路径，后续也会用到这个路径。 具体的复制方式可以选择直接访问Github来找这个项目，或者Linux终端上用git clone命令来克隆项目，都可以，只要下载好这个项目就可以。<br>

3. 下载好了ESP-idf之后需要继续下载一些官方指定如果要使用ESp-idf所需要的工具，这些工具和下载方式官方已经写成了下载脚本，并放在了esp-idf这个项目中， 所以在linux系统下，我们需要从终端进入这个项目路径(cd) 然后执行这个脚本就可以了 
 ``` linux
    ./install.sh esp32    #注意这里esp32表示的是你将要使用ESP32板子的型号，比如我用的基于ESP32 P4的开发板，那我就要换成esp32p4
```  
<br>

下载好所有工具之后，就可以到下一步了

## 3. ESP32 项目构建过程和项目结构

1. 项目结构:<br>
esp32项目中有三种重要的元素，源代码main, 组件库components, CMakeLists.txt文件。 一般也就这三个东西， 大概知道里面是写什么的，有什么用就行 <br>
    （a）源代码就是有main.c的文件夹。 里面也许会有main.h来做头文件，也可以不用。但是一定要有CMakeLists.txt和main.c 这两个文件 main.c就是程序入口 非常重要。 CMakeLists.txt文件是构建esp32项目不能少的配置文件，可以理解为在构建项目的过程中，这个文件告诉了构建脚本这个文件夹下的.c .h需要什么样的配置。 如果配置和代码不匹配，就会构建失败报错。 常见的错误例子有代码中调用的API没有在CMakeList里面声明, CMakeLists.txt有等级 下面是非项目级和项目级的内容(项目级的CMakeLists.txt里的内容和非项目级的不一样，毕竟构建模块和构建整个项目需要的配置肯定不同)
    ```  
            idf_component_register(                    //非项目级
            SRCS "main.c"
            REQUIRES my_spi my_mcpwm
            INCLUDE_DIRS "."
        )
    ```     
    ```  
            cmake_minimum_required(VERSION 3.16)       //项目级
            include($ENV{IDF_PATH}/tools/cmake/project.cmake)
            idf_build_set_property(MINIMAL_BUILD ON)
            project(All_funcs_test)    
    ```



## 4. 外设组件
### MCPWM 

Connection :

```
      ESP Board              BM50 Motor            12V
+-------------------+     +---------------+         ^
|          PWM_GPIO +-----+PWM        VCC +---------+
|          DIR_GPIO +-----+DIR            |
|        BRAKE_GPIO +-----+BRAKE          |
|                   |     |               |
|         encoder_a +-----+a_channel      |
|         encoder_b +-----+b_channel      |
|                   |     |               |
|               GND +-----+GND            |
+-------------------+     +---------------+
```

### Wifi

esp32 wifi













 
