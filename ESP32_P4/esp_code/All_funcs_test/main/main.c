#include <stdio.h>
#include "my_spi.h"
#include "my_mcpwm.h"


void app_main(void){

    mcpwm_motor_test();
    
}

/*
ESp32 moduleP4 这个开发板主核是P4，P4没有蓝牙功能，就很烦，板子上加入了一个C6模块用来无线通信。
https://github.com/espressif/esp-hosted-mcu/blob/main/README.md 这个开源仓库解决的就是这种问题
主MCU和通信从机模块的方式来实现主MCU可以无线通信的功能




*/