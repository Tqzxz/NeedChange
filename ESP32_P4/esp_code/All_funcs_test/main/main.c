#include <stdio.h>
#include "my_spi.h"
#include "my_mcpwm.h"
#include "esp_log.h"

#define PWM_PIN GPIO_NUM_36
#define DIR_PIN GPIO_NUM_32
#define BRAKE_PIN GPIO_NUM_25

void app_main(void){

    int mcpwm_group_id      = 0;
    int gpio_num            = PWM_PIN;
    int timer_resolution_hz = 1000000; 
    int timer_period_ticks  = 20000;
    int comp_value          = 10000; 

    mcpwm_timer_handle_t timer   = create_mcpwm_timer(mcpwm_group_id, timer_resolution_hz, timer_period_ticks);
    mcpwm_oper_handle_t oper     = create_mcpwm_operator(mcpwm_group_id, timer);
    mcpwm_gen_handle_t gen       = create_mcpwm_generator(oper, gpio_num);
    mcpwm_cmpr_handle_t comparator = create_mcpwm_comparator(oper);
    set_gen_actions(gen, comparator);
    mcpwm_timer_enable(timer);
    ESP_ERROR_CHECK(mcpwm_timer_start_stop(timer,MCPWM_TIMER_START_NO_STOP));

    ESP_LOGI("MCPWM", "PWM started on GPIO %d", gpio_num);

    gpio_config_t gpio_config1 = {
        .pin_bit_mask = 1ULL << DIR_PIN,
        .mode  =  GPIO_MODE_OUTPUT,
    };

    gpio_config_t gpio_config2 = {
        .pin_bit_mask = 1ULL << BRAKE_PIN,
        .mode  =  GPIO_MODE_OUTPUT,
    };

    gpio_config(&gpio_config1);
    gpio_config(&gpio_config2);

    int i = 0;
    while(1){
        // 速度1
        gpio_set_level(DIR_PIN, 1);
        set_comp_value(comparator, comp_value); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*2); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*4); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*8); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*16); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        gpio_set_level(DIR_PIN,0);
        set_comp_value(comparator, comp_value*8); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*4); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*2); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*2);
        gpio_set_level(BRAKE_PIN,1);
        i++;

        if(i == 2){
            break;
        }
    }
}