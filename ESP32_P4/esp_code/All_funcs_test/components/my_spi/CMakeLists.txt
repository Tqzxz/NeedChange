idf_component_register(
  SRCS "my_spi.c"
  REQUIRES esp_driver_spi
  PRIV_REQUIRES  esp_driver_gpio
  INCLUDE_DIRS "."
)