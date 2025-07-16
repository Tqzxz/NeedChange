# freeRtos

## 1. ESP存储硬件结构
DRAM也叫 Dynamic random access memo <br>
动态随机访问内存，数字电路中有学过这种电路，特点是需要不断刷新电压水平来保存信息，断电不保护数据。优点是结构简单，不需要太多晶体管，相比于SRAM. <br>

1.官方是这样描述的: 非常量静态数据（.data 段）和零初始化数据（.bss 段）由链接器放入内部 SRAM 作为数据存储。此区域中的剩余空间可在程序运行时用作堆。 <br>
所以一般情况，我们执行 idf.py build后， 编译器会根据程序对程序中的数据进行区分存储， 程序中的非常量静态数据，0初始化数据都会被保存在这里 <br>

2. const关键字表示常量， 所以程序中没有用const关键字描述的变量都属于非常量， 而用户初始化非0的全局和局部变量会被归于非常量静态数据，相反初始化为0的归于0初始化数据

## 2. Intro
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
            7. 任务分配核(0/1)  <br>
## 3. freeRtos的一些常见函数 
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
<br>

## 4. 队列（系统中协调任务之间数据通信的方式，感觉是异步的，也可以是同步的）
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
<br>

## 5. 信号量 

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

 ```





































            

