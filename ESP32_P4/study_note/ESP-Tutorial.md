

## ESP存储硬件结构

# DRAM也叫 Dynamic random access memo <br>
动态随机访问内存，数字电路中有学过这种电路，特点是需要不断刷新电压水平来保存信息，断电不保护数据。优点是结构简单，不需要太多晶体管，相比于SRAM. <br>

1.官方是这样描述的: 非常量静态数据（.data 段）和零初始化数据（.bss 段）由链接器放入内部 SRAM 作为数据存储。此区域中的剩余空间可在程序运行时用作堆。 <br>
所以一般情况，我们执行 idf.py build后， 编译器会根据程序对程序中的数据进行区分存储， 程序中的非常量静态数据，0初始化数据都会被保存在这里 <br>

2. const关键字表示常量， 所以程序中没有用const关键字描述的变量都属于非常量， 而用户初始化非0的全局和局部变量会被归于非常量静态数据，相反初始化为0的归于0初始化数据


## freeRtos

# 1. Intro
  freeRtos中是按照执行任务来执行模块化程序的， 任务存在一下状态： <br>
  (A) 运行状态 <br>
  (B) 准备状态 <br>
  (C) 阻塞状态 <br>
  (D) 挂起状态 <br>

  在ESP-idf中， 我们可以使用 xTaskCreatePinnnedToCore() 这个函数来创建一个任务
  函数参数为 1. 任务函数指针    <br>
            2. 自定义任务名称  <br>
            3. 自定义任务堆栈大小  单位以字节为单位  <br>
            4. 给任务传递的参数  <br>
            5. 任务优先级         取值范围是 0 - (configMAX-PRIORITIES-1)  <br>
            6. 任务返回句柄       可以理解为是任务对象， 这个对象中包含一些成员信息，后续可以通过引用这个对象来修改这个任务的属性  <br>
            7. 任务分配核(0/1)  <br>
# 2. freeRtos的一些常见函数 
  (A) XTaskGetTickCount()                            : 获取当前系统的节拍数
  (B) vTaskDelayUntil(&系统节拍， int 节拍数)         ： 根据系统节拍，精确延时
  (C) VTaskDelay()                                   : 简单延时, 执行后，任务将会成为挂起状态，参数xTicksToDelay表示延时多少个节拍
  (D) pdMS_TO_TICKS()                                ： 把ms毫秒数转换为系统节拍数

  test_task.c
  include "freertos/task.h"
  include "freertos/FreeRTOS.h"
  incldue "esp_log.h"
'''C
  void taskA(void* params){
    while(1){
        ESP_LOGI("...");
        vTaskDelay(pdMS_TO_TICKS(500))  // 挂起任务500ms
    }
  }

  void app_main(){
    xTaskCreatePinnedToCore(taskA,"taks_test",....);
  }
''' <br>
# 3. 队列（系统同步）
系统同步是指： 不同任务之间的系统工作方式，协调资源，避免多个任务之间的数据竞争等冲突情况





































            

