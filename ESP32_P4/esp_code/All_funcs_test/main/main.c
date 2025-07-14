#include <stdio.h>
#include "driver/sdmmc_host.h"
#include "my_spi.h"
#include "my_mcpwm.h"

#define SDIO_CLK     18
#define SDIO_CMD     19
#define SDIO_DAT0    14
#define SDIO_DAT1    15
#define SDIO_DAT2    16
#define SDIO_DAT3    17

void app_main(void){

    // mcpwm_motor_test();
    
}

/*
ESp32 moduleP4 这个开发板主核是P4，P4没有蓝牙功能，就很烦，板子上加入了一个C6模块用来无线通信。
https://github.com/espressif/esp-hosted-mcu/blob/main/README.md 这个开源仓库解决的就是这种问题
主MCU和通信从机模块的方式来实现主MCU可以无线通信的功能

微雪P4 module在开发板上已经封装好了C6芯片，并且C6模块已经烧录了固件

1. 添加组件 espressif/esp_wifi_remote 和 espressif/esp_hosted 到 P4上
  这两个组件提供了新的无线通信功能的API，底层原理大概就是 主机通过RPC底层通过传输通道给从机发送指令，从机进行通信，然后通过传输通道将数据传回主机
  前提是原组件中没有无线通信组件。

2. 硬件连接传输通道配置 (SPI, SDIO), P4 module是采用了SDIO的连接方式
配置方式参考这个仓库https://github.com/espressif/esp-hosted-mcu/blob/main/docs/sdio.md

3. 添加好组件，并初始化配置好SDIO硬件连接之后，就可以在主程序中使用esp_hosted_... 等无线通信函数来通信，虽然底层是通信调用C6模块


*/