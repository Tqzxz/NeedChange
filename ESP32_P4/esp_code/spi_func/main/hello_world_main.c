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

#define PIN_NUM_MISO  26
#define PIN_NUM_MOSI  48
#define PIN_NUM_CLK   53
#define PIN_NUM_CS    47

void init_spi(spi_bus_config_t* buscfg, spi_device_interface_config_t* devcfg){

    buscfg->mosi_io_num = PIN_NUM_MOSI;
    buscfg->miso_io_num = PIN_NUM_MISO;
    buscfg->sclk_io_num = PIN_NUM_CLK;
    buscfg->quadwp_io_num = -1;
    buscfg->quadhd_io_num = -1;
    buscfg->max_transfer_sz = 4096;            //  总线最大传输长度

    devcfg->clock_speed_hz = 1 * 1000 * 1000;  //  时钟频率
    devcfg->mode = 0;                          //  SPI 模式 0
    devcfg->spics_io_num = PIN_NUM_CS;
    devcfg->queue_size = 1;
    devcfg->flags = 0;
    devcfg->pre_cb = NULL;
    devcfg->post_cb = NULL;

    return 
}

void app_main(void)
{
    // Initialize SPI bus configuration
    spi_bus_config_t              spi_bus_config;
    spi_device_interface_config_t spi_device_config;

    






}
