/*
 * SPDX-FileCopyrightText: 2010-2022 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: CC0-1.0
 */

#include <stdio.h>
#include "driver/spi_master.h"
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "my_spi.h"
 


/**
 * @brief buscfg/devcfg ： SPI通信总线和设备的配置结构体变量
 * 
 * spi_init 函数是 my_spi.c 中唯一用来初始化 SPI 总线和设备的函数。
 * 
 */

spi_device_handle_t spi_init(void){

    spi_device_handle_t spi = NULL;    // SPI设备句柄
    esp_err_t ret;
    
    spi_bus_config_t buscfg = {   // SPI通信总线配置结构体

        .miso_io_num = PIN_NUM_MISO,    // MISO引脚绑定
        .mosi_io_num = PIN_NUM_MOSI,    // MOSI引脚绑定
        .sclk_io_num = PIN_NUM_CLK,     // SCLK引脚绑定
        .quadwp_io_num = -1,            // Quad WP
        .quadhd_io_num = -1,            // Quad HD
        .max_transfer_sz = 4096         // 最大传输大小，0表示默认值
    };

    spi_device_interface_config_t devcfg = {   // SPI设备接口配置结构体

        .clock_speed_hz = 1000000,       // SPI时钟频率，1MHz
        .mode = 0,                       // SPI模式
        .spics_io_num = PIN_NUM_CS,      // SPI片选型号绑定
        .queue_size = 1,                 // 消息发送事务队列大小
        .flags = 0,
        .pre_cb = NULL,                  // 发送前回调函数
        .post_cb = NULL,                 // 发送后回调函数
    };  

    ret = spi_bus_initialize(SPI_HOST, &buscfg, SPI_DMA_CH_AUTO);
    assert(ret == ESP_OK);

    ret = spi_bus_add_device(SPI_HOST, &devcfg, &spi);
    assert(ret == ESP_OK);

    return spi;

}                
    

char* spi_pack_data(char* data, int data_length){



    return 
}


   


    

    