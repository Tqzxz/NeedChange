idf_component_register(
    SRCS "main.c"
    REQUIRES my_spi my_mcpwm, esp_driver_sdmmc
    INCLUDE_DIRS "."
)
