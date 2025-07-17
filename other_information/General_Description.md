
### To-do list
- [ ] 2 episode Freertos
- [ ] 学习一个外设


# Project Contents:

***
## 1. Project Description <br>
  
  (1) 车底盘由具有车轮编码器的电机驱动履带，橡胶轮胎， 可以进行灵活的移动（直线，直角，斜线，曲线）                                                         <br>
  (2）目前计划的车身可以控制： (1)底座电机的控制 （2）车前方旋转齿轮电机  （3）其他装置（需要想想怎么设计）（4）飞行物射击器（需要想想怎么设计）                <br>
  (3) 属性  ：电量，能量，虚拟损耗程度, 车辆发热情况（当车辆过热将执行一些debuff， 比如降低属性，关闭某些车辆功能）                                         <br>  
  (4) 系统  ：车身操作系统作为车身设备和用户之间的接口 同时需要和外部裁判系统通信                                                                         <br>
  (5) 等级成长性：任何可以修改的数值都可以作为可以成长的属性, e.g( 齿轮旋转速度， 车子移动速度， 发射飞行物的速度)                                           <br>
  (6) 车身可以被攻击到侧翻， 如果侧翻 长时间出局  电量0%->回到充电点更换  被飞行物攻击，被旋转齿轮攻击到一些点位会提高损耗度，损耗程度100% -> 回到修理点   消耗电量，能量，损耗值来 (1)短暂提高属性 (2)释放更高属性的技能 <br>
  (7) 控制方式：(1) 基础遥控器 (2) 更逼真的驾驶台 --> 前提条件： 需要使用一个认证过的钥匙启动 （钥匙和车绑定）                                              <br>
  
  玩家控制： <br>
  (1) 玩家可以踩控制车辆移动的踏板  以及一个综合控制台， 比如控制车的攻击， 以及其他辅助功能  <br>
  (2) 玩家视角： 车辆驾驶的视角以及一些辅助信息。   <br>
  (3) 反馈系统： 驾驶位置会根据实际车身收到的信息进行反馈 <br>

  对战机制： <br>
  (1) 阶段制  可以有 (1)擂台对战阶段，胜负规则：(1)出赛场范围 (2)被撞击侧翻 （3）损耗度100%  （2）护送目标阶段 等等 <br>

``` C
/*
  LinkeFiniteStateMachine  statecode 00: 待机状态，关闭所有可以关掉的功能
                           statecode 01: 启动运动模式，开启一些必要的监听，响应等功能，部分功能关闭
                           statecode 02: 启动竞技模式，开启所有功能

*/
```

## 2. ESP-IDF and APIs Fully explaination <br>

> __The Aim for this part is to explain how some of ESP32 modules works and show the correct way of using their ESP APIs(SPI,MCPWM) and how build project and run project on a ESP32 board__<br>   

### 2.1 准备工作
  1. 需要有一个Linux系统/虚拟机环境, 第一步需要先在终端输入一些下载工具的指令<br>
   ``` linux
    sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
  ```  
  下载必要工具比如 python3, cmake, venv 等等， 需要注意 Cmake需要3.16及以上的版本，老版本Linux系统运行指令可能下载的是老版本Cmake, 需要先升级系统或者直接下载Cmake3, 有些工具比如python3大概率Linux系统是自带，有些工具有就可以不用下，怎么  系统升级，查看是否下载了某些工具这些指令上网一搜就有<br>
  
  2. 下载好了这些工具之后，就可以来下载ESP32官方提供的开发工具 ESP-IDF 了，这个工具里面有非常多的内容， 其中包括ESP32底层的源代码，编译你项目的脚本程序，等等。这个项目就是从ESP32底层源码向上抽象了一层，将一些可以合并的函数合并成一个功能。在github找到ESP32IDF仓库https://github.com/espressif/esp-idf之后，把这个项目复制到本地，并且一定要记住存放这个项目的路径，后续也会用到这个路径。具体的复制方式可以选择直接访问Github来找这个项目，或者Linux终端上用git clone命令来克隆项目，都可以,只要下载好这个项目就可以。 <br>
  
  3. 下载好了ESP-idf之后需要继续下载一些官方指定如果要使用ESp-idf所需要的工具，这些工具和下载方式官方已经写成了下载脚本，并放在了esp-idf这个项目中， 所以在linux系统下，我们需要从终端进入这个项目路径(cd) 然后执行这个脚本就可以了 
   ``` linux
      ./install.sh esp32    #注意这里esp32表示的是你将要使用ESP32板子的型号，比如我用的基于ESP32 P4的开发板，那我就要换成esp32p4
  ```
***
### 2.2 ESP32 项目构建过程和项目结构
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
***
### 2.3 外设组件 <br>

#### 2.3.1 MCPWM 

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
***
#### 2.3.2 Wifi
wifi工作模式有 AP, STA, AP+STA,等等 <br>
AP模式： AP模式下，设备被定义为无线网络中的节点，会向外广播SSID,允许其他设备对它进行连接(路由器就是AP模式下的应用)
STA模式：STA模式下，设备被定义为无线网络中的客户端/用户，可以进行AP扫描，并尝试连接，并且通过认证后可以通过AP设备访问其他设备,进行数据的交换
```C
/*
Wifi热点工作流程 AP 模式为例
    首先整体通信框架的上层是我们的应用程序 app 
    中层是通信接口协议栈 LwIP stack
    底层是wifi 驱动程序

    

*/
/*
include <stdio.h>
include "nvs_flash.h"
include "esp_wifi.h"
include "esp_log.h"
include "esp_event.h"
include "esp_err.h"

void app_main(void){

  //(1). 初始化 nvs, 就是一些联网配置
  // 为什么需要nvs, 主要是为了保存SSID 密码到nvs, esp-idf会再系统下一次上电用nvs中的这个来连接wifi
    ESP_ERROR_CHECK(nvs_flash_init());    
  //(2). 初始化TCP/IP协议栈
    ESP_ERROR_CHECK(esp_netif_init());

  //(3). 创建事务循环
    ESP_ERROR_CHECK(esp_event_loop_create_default());

  //(4). 创建STA对象，进而才能使用STA通信模式
    esp_netif_create_wifi_sta();

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));

    // (5) 注册事件响应
    esp_event_handler_register(WIFI_EVENT,ESP_EVENT_ANY_ID,wifi_event_handle,NULL);
  
*/

}
```
***
#### 2.3.3 SPI:
传输速率很快的设备间通信方式。 由一台被定义为主机( Master )的设备主导SPI传输的通道。通道连接1个或者多个从机。 通道由4根线组成
  (1) SCLK    : 同步时钟信号 <br>
  (2) MOSI    : 主机传输信息到从机的信号线 <br>
  (3) MISO    : 从机传输信息到主机的信号线 <br>
  (4)  CS     : 片选信号( 从机选择信号 )  <br>

  SPI的传输是时钟同步的，并不是异步的, (2)和(3)信号线说明，信息传输是双向的, (4)则是说明 (2),(3) 传输线是 多个从机公用的， 只允许同一时刻只能和一个从机进行通信，但是可以切换. 特点总结: 高速率，单主机多从机，同步双工 <br>

***
#### 2.3.4 GPIO和PWM占空比调制:
 ``` C
/*
在程序中使用GPIO需要加入driver/gpio.h这个头文件。 下面是示例代码
控制一个外设的大概过程就是 1.先配置一些外设需要的硬件和参数，在配置过程中，如果需要，有些硬件的配置需要其他已经配置好的硬件 2. 启动 就这么简单
LEDC控制的配置流程，官方来说，最好按照以下步骤来配置
(1) 配置定时器， 就有疑问了，控制LED，定时器用来干什么？ 定时器其实是和PWM挂钩的
(2) 配置通道， 这里这个通道有点像什么呢， 就是central unit， 它接收定时器的信号，并输出PWM信号
(3) 配置好定时器，和通道，理论上，用户定义的GPIO引脚已经可以输出一个恒定占空比的PWM信号了， 为了达到呼吸灯的效果，用户有两个选择
  一个是通过动态修改输出的PWM占空比来实现 大概就是 （1）ledc_set_duty (2) ledc_update_duty 这两个函数
  一个是通过硬件设置 fade, 示例代码中介绍的就是这种方式。 fade硬件可以从官方结构图中看出是和通道所连接的，所以每个通道都可以有一个fade硬件
*/
#include "driver/gpio.h"
#include <stdio.h>
#include "freertos/task.h"
#include "freertos/FreeRTOS.h"
#include "driver/ledc.h"


#define FULL_EV_BIT   BIT0
#define EMPTY_EV_BIT  BIT1
static EventGroupHandle_t ledc_event_handle;  //ledc完成呼吸灯事件组句柄

#define LED_GPIO GPIO_NUM_17

bool IRAM_ATTR ledc_finish_cb(const ledc_cb_param_t* param, void* user_arg){
    BaseType_t taskWoken;
    if(param->duty){
        xEventGroupSetBitsFromISR(ledc_event_handle,FULL_EV_BIT,&taskWoken);
    }else{
        xEventGroupSetBitsFromISR(ledc_event_handle,EMPTY_EV_BIT,&taskWoken);
    }
}

void led_run_task(void* param)
{
    int gpio_level = 0;
    while(1){
        ev = xEventGroupWaitBits(ledc_event_handle,FULL_EV_BIT|EMPTY_EV_BIT,pdFALSE,pdMS_TO_TICKS(5000));
        if(){
            ...
        }else{
            ...
        }
    }
}

void app_main(void)
{
  // 先初始化配置GPIO引脚
    gpio_config_t led_cfg = {
        .pin_bit_mask = (1<<LEF_GPIO),  // 位掩码
        .pull_up_en   = GPIO_PULLUP_DISABLE,
        .pull_down_en = GPIO_PULLDOWN_DISABLE,
        .mode         = GPIO_MODE_OUTPUT,
        .intr_type    = GPIO_INTR_DISABLE 
    };
    gpio_config(&led_cfg);
    // xTaskCreatePinnedToCore(....);

//上面代码是控制GPIO引脚输出模式的输出电压的示例代码，下面是通过PWM占空比调制的方式使得输出PWM波形，让LED灯产生渐变亮度

//初始化定时器
    ledc_timer_config_t led_timer= {
        .speed_mode = LED_LOW_SPEED_MODE,
        .timer_num  = LEDC_TIMER_0,
        .clk_cfg    = LEDC_AUTO_CLK,
        .freq_hz    = 5000,
        .duty_resolution  = LEDC_TIMER_13_BIT
    };
    ledc_timer_config(&lef_timer);

//初始化通道
    ledc_channel_config_t ledc_channel = {
        .speed_mode = LEDC_LOW_SPEED,
        .channel    = 0,
        .timer_sel  = LEDC_TIMER_0,
        .gpio_num   = LED_GPIO,
        .duty       = 0,
        .intr_type  = LEDC_INTR_DISABLE
    };
    ledc_channel_config(&ledc_channel);

// 为了使用fade硬件功能，第一步需要先下载fade
    ledc_fade_func_install(0);
// 然后进行fade设置函数( 官方给出了三个设置函数，选择一个就好）
    ledc_set_fade_with_time(LEDC_LOW_SPEED,LEDC_CHANNEL_0,0,2000);
// 最后启动fade
    ledc_fade_start(LEDC_LOW_SPEED,LEDC_CHANNEL_0,LEDC_FADE_NO_WAIT);
 // 下面再写回调函数,注册回调函数... emm我觉得吧 其实ledc.h这个库和PWM库的内容真差不多，有定时器，通道，等等什么的， 其实自己写呼吸灯，不需要这么复杂的吧
    ledc_cbs_t cbs = {
        .fade_cb = ledc_finish_cb
    };
    ledc_cb_register(LEDC_LOW_SPEED,LEDC_CHANNEL_0,&cbs,NULL);
    xTaskCreatePinnedToCore(led_run_task,"led",2048,NULL,3,NULL,1);
}
 ```
***

## 3. FreeRTOS Tutorial

### 3.1 ESP存储硬件结构
DRAM也叫 Dynamic random access memo <br>
动态随机访问内存，数字电路中有学过这种电路，特点是需要不断刷新电压水平来保存信息，断电不保护数据。优点是结构简单，不需要太多晶体管，相比于SRAM. <br>

1.官方是这样描述的: 非常量静态数据（.data 段）和零初始化数据（.bss 段）由链接器放入内部 SRAM 作为数据存储。此区域中的剩余空间可在程序运行时用作堆。 <br>
所以一般情况，我们执行 idf.py build后， 编译器会根据程序对程序中的数据进行区分存储， 程序中的非常量静态数据，0初始化数据都会被保存在这里 <br>

2. const关键字表示常量， 所以程序中没有用const关键字描述的变量都属于非常量， 而用户初始化非0的全局和局部变量会被归于非常量静态数据，相反初始化为0的归于0初始化数据

### 3.2 Intro
  freeRtos中是按照执行任务来执行模块化程序的， 任务存在一下状态： <br>
  (A) 运行状态 
  <br>
  (B) 准备状态 
  <br>
  (C) 阻塞状态
  <br>
  (D) 挂起状态 
  <br>

  在ESP-idf中， 我们可以使用 xTaskCreatePinnnedToCore() 这个函数来创建一个任务
  函数参数为 1. 任务函数指针    <br>
            2. 自定义任务名称  <br>
            3. 自定义任务堆栈大小  单位以字节为单位  <br>
            4. 给任务传递的参数  <br>
            5. 任务优先级         取值范围是 0 - (configMAX-PRIORITIES-1)  <br>
            6. 任务返回句柄       可以理解为是任务对象， 这个对象中包含一些成员信息，后续可以通过引用这个对象来修改这个任务的属性  <br>
            7. 任务分配核(0/1) 
            
***
### 3.3 freeRtos的一些常见函数 
  (A) XTaskGetTickCount()                            : 获取当前系统的节拍数      <br>
  (B) vTaskDelayUntil(&系统节拍， int 节拍数)         ： 根据系统节拍，精确延时    <br>
  (C) VTaskDelay()                                   : 简单延时, 执行后，任务将会成为挂起状态，参数xTicksToDelay表示延时多少个节拍  <br>
  (D) pdMS_TO_TICKS()                                ： 把ms毫秒数转换为系统节拍数  <br>

``` C
  //test_task.c 
  #include "freertos/task.h"
  #include "freertos/FreeRTOS.h"
  #incldue "esp_log.h"
  

  void taskA(void* params){
    while(1){
        ESP_LOGI("...");
        vTaskDelay(pdMS_TO_TICKS(500))  // 挂起任务500ms
    }
  }

  void app_main(){
    xTaskCreatePinnedToCore(taskA,"taks_test",....);
  }
```
***

### 3.4 任务间协调通信方式(1/4) 队列（系统中协调任务之间数据通信的方式，感觉是异步的，也可以是同步的）
系统同步是指： 不同任务之间的系统工作方式，协调资源，避免多个任务之间的数据竞争等冲突情况 <br>

  关于队列的系统函数，所有到目前为止和下面提到的函数都可以在espressif乐鑫官方找到函数完全的定义 <br>

  QueueHandle_t xQueueCreate(param1, param2);     //创建队列函数                param1: UBaseType_t uxQueueLength 队列容量  param2: UBaseType_t uxltemSize 队列元素占内存的大小(in byte) <br>
  BaseType_t xQueueSend(param1, param2, param3);  //向指定队列的头部发送数据     param1: QueueHandle_t xQueue  指定队列的句柄 param2: const void* content 要发送的消息指针 param3: TickType_t WaitTicks 等待时间(in tick)   <br>  
  BaseType_t xQueueSendToBack();                  //向指定队列的尾部发送数据     参数设置和上面一样 <br>
  BaseType_t xQueueReceive(param1,param2,param3); //向指定队列接收数据          param1: QueueHandle_t xQueue  指定队列的句柄 param2: void* buffer 接收消息缓冲区 param3: TickType_t WaitTicks 等待时间 <br>
  BaseType_t xQueueSendFromISR();                 //向队列发送信息的中断版本 <br>

  下面是一个队列的示例代码
  ``` C
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"
#include "esp_log.h"
#include <string.h>

//声明全局队列变量
QueueHandle_t my_queue = NULL;

//自定义queue_data_t结构体类型，作为发送接收的数据类型
typedef struct
{
   //只有一个int value
   int value;
}queue_data_t;

//任务A while循环，当xQueueReceive从全局队列 my_queue中读取数据正常返回 pdTRUE之后，打印读取数据的value
void taskA(void* param){
    queue_data_t  data;
    while(1){
      if(pdTRUE == xQueueReceive(my_queue,&data,100)){
        ESP_LOGI("queue received value:&d" , data.value);
      }
    }
}

//任务B while循环 初始化data_send发送的数据类型 value = 0， 每过1000个ticks，value自增1，然后继续发送
void taskB(void* param){
    queue_data_t data_send;
    memset(&data_send,0,sizeof(queue_data_t));
    while(1){
      xQueueSend(my_queue,&data_send,100);
      vTaskDelay(1000);
      data_send.value++;
    }
}

void app_main(void){

    //给全局my_queue创建实例
    my_queue = XQueueCreate(10,sizeof(queue_data_t));
    // 设置任务到1核，任务核
    xTaskCreatePinnedToCore(taskA,'taskA',2048,NULL,3,NULL,1);
    // 设置任务到1核，任务核
    xTaskCreatePinnedToCore(taskB,'taskB',2048,NULL,3,NULL,1);

}

  ```
***

### 3.5 任务间协调通信方式(2/4) 信号量 

信号量形象地解释： 现在有一个全局雨伞池，有一定数量的雨伞。 每个任务可以向雨伞池中尝试取出雨伞。 当池中没有雨伞时，需要等待有人归还雨伞才可再取走 <br>
雨伞就是信号量. 信号量又分为二进制，计数，互斥类型的信号量，一一解释 <br>
(A) 二进制信号量， 就是表示信号量池中只有一个信号量 <br>
(B) 计数信号量，   表示信号量中有多个信号量  <br>
(C) 互斥锁信号量， 和二进制信号量类似， 但是实现了优先级的继承。  <br>

互斥锁的优先级继承: 三个任务(H,M,L)优先级依次下降， 当L先运行并抢占了互斥锁信号量之后， 时间切片任务调度器继续选择下一个时间片要执行的任务，为任务H, 任务H依赖于互斥信号量，因此此次任务A被阻塞 <br>
导致任务调度器接下来选择的任务是M， 因为M 优先级高于L, 那么问题就是 任务A需要等待任务L执行到释放锁的代码， 但是任务M一直在抢占运行时间片。 导致M任务变相的拖慢了任务A的执行 <br>
解决方法就是当高优先级任务向互斥锁请求锁失败后，将当前拥有锁的任务优先级提升到高优先级任务的等级，知道释放锁之后再降低为原来的优先级。<br>

 ``` C
//关于信号量的API函数
// 1. 创建二进制信号量
SemaphoreHandle_t xSemaphoreCreateBinary(void); 创建成功后，返回一个信号量句柄

// 2. 创建计数信号量
SemaphoreHandle_t xSemaphoreCreateCounting(void);

// 3. 获取信号量
xSemaphoreTake(param1,param2);  //param1: 信号量句柄 SemaphoreHandle_t , param2: 等待时间(in ticks)

// 4. 释放信号量
xSemaphoreGive(param1);         //param1: 信号量句柄 SemaphoreHandle_t

// 5. 删除信号量
void xSemaphoreDelete(SemaphoreHandle_t sema);

// 6. 互斥锁相关
SemaphoreHandle_t xSemaphoreCreateMutex(void);

//下面是示例代码
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "driver/gpio.h"
#include "esp_log.h"
#include "dh11.h"

SemaphoreHandle_t my_binary_sema;        // 声明全局二进制信号量

void taskA(void* param){
    while(1){
        // 每隔1000个tick时间，taskA任务释放全局二进制信号量
        xSemaphoreGive(my_binary_sema);
        vaTaskDelay(1000);
    }
}

void taskB(void* param){
    while(1){
        if(pdTRUE == xSemaphoreTake(my_binary_sema,portMAX_DELAY)){
            ESP_LOGI("taskB take binary sema successful");
        }
    }
}

void app_main(void){

    my_binary_sema = xSemaphoreCreateBinary();
    // 设置任务到1核，任务核
    xTaskCreatePinnedToCore(taskA,'taskA',2048,NULL,3,NULL,1);
    // 设置任务到1核，任务核
    xTaskCreatePinnedToCore(taskB,'taskB',2048,NULL,3,NULL,1);

}


 ```
***
### 3.6 任务间协调通信方式(3/4) Event 事件组 和 任务间协调通信方式(4/4) 直达任务通知

1. 事件组
 事件组是由一系列个事件位组成的，每一个事件位用一个编号来标识， 事件位用来表示某个事件是否发生， 如果发生事件位的值为1，反之为0. emm 感觉就是一个flag数组，每一个flag的值都表示当前索引所代表的事件是否发生 <br>
 ``` C
 /*
    事件组常用API
    1. EventGroupHandlr_t xEventCreate(void) //创建事件组对象，返回
    2. EventBits_t xEventGroupWaitBits(param1,param2,param3,param4,param5);
      //param1: EventGroupHandle_t 事件组句柄  param2: const EventBits_t 等待的事件位  param3:BaseType_t 是否清除事件位  param4: BaseType_t 是否等待所有  param5: 等待时间
      //事件组中采用的是EventBits_t这个类型的8或者24位（通常24）的无符号整型数据来保存8或者24个事件位。 采用16进制表示方式。 一般采用下面这样的方法来定义一个事件位，以及判定等待事件位逻辑
      #define BIT_0 (1UL << 0)
      #define BIT_1 (1UL << 1)  // 1UL << 十进制位 这样提高了可读性
      为了同时判定多个事件位， 我们可以用 | 逻辑或运算来表示 比如同时等待事件1，事件2就写 (BIT_0 | BIT_1)
      当等待条件在最大等待时间之前满足时，函数返回 clear操作前的事件组的24位值， 然后我们可以通过用 & 与运算来获得关注的事件位，比如这里我们好奇事件0，事件1
      就可以 ux_bits = xEventGroupWaitBits(...)
            if (uxbits & BIT_0) != 0 ...
   事件组同步函数 例子
    xEventGroupSync(
            xEventBits,     /* The event group being tested. */
            TASK_1_BIT,     /* The bits within the event group to wait for. */
            ALL_SYNC_BITS,  /* The bits within the event group to wait for. */
            portMAX_DELAY); /* Wait a maximum of 100ms for either bit to be set. */
    同步函数和等待函数类似，执行到同步函数时，如果没有满足等待条件会进入阻塞状态等待。 不同的是，执行到这里，函数会自动将这个任务事件位设置为1， 并进入等待，等待条件是其他相关的所有同步任务也执行到了这个函数
    最后执行到这里的同步函数，会唤醒所有同步任务，并且自动会把所有任务的事件位clear掉
*/
```

