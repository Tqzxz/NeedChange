idf_component_register(
    SRCS "main.c"
    REQUIRES my_spi my_mcpwm
    INCLUDE_DIRS "."
)
