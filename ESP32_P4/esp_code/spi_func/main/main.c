#include <stdio.h>
#include "my_spi.h"

void app_main(void){

    spi_device_handle_t my_spi = spi_init();

    if (!my_spi) {
        printf("Failed to initialize SPI device.\n");
        return;
    }
    printf("Hello, ESP32!\n");

}