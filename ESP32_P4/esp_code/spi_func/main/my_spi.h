#ifndef MY_SPI_H
#define MY_SPI_H

#include "driver/spi_master.h"

////////////////////////////////////////////////////////////////////////////////////////////////////////////
// ////////////// Following configuration based on ESP32 P4 module board ///////////////////////////////////

#define SPI_HOST      SPI2_HOST   // 选择 SPI2_HOST 或者 SPI3_HOST 来作为 SPI 主机
#define PIN_NUM_MISO  26          // MISO ：信号接收信号     （26,48,53,47都是通用可编程GPIO引脚号）
#define PIN_NUM_MOSI  48          // MOSI ：信号发送信号
#define PIN_NUM_CLK   53          // SCLK ：主机时钟信号
#define PIN_NUM_CS    47          // CS   : 多从机片选信号

#define SPI_DATA_PACKAGE_LEN   10    
////////////////////////////////////////////////////////////////////////////////////////////////////////////


spi_device_handle_t spi_init(void);

char* spi_pack_data(char* data, int data_length);




#endif

