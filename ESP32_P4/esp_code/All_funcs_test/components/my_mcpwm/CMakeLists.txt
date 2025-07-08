idf_component_register(
  SRCS "my_mcpwm.c"
  REQUIRES driver esp_driver_mcpwm esp_driver_gpio
  INCLUDE_DIRS "."
)
