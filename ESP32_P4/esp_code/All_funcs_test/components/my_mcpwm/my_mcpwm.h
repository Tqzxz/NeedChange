
#include "driver/mcpwm_prelude.h"
#include "driver/gpio.h"

#define INIT_OK     1
#define INIT_ERR    0

#define PWM_PIN GPIO_NUM_36
#define DIR_PIN GPIO_NUM_32
#define BRAKE_PIN GPIO_NUM_25

mcpwm_timer_handle_t create_mcpwm_timer(int mcpwm_group_id,int resolution_hz, int period_ticks);

mcpwm_oper_handle_t create_mcpwm_operator(int mcpwm_group_id, mcpwm_timer_handle_t timer);

mcpwm_gen_handle_t create_mcpwm_generator(mcpwm_oper_handle_t oper, int pwm_gpio_num);

mcpwm_cmpr_handle_t create_mcpwm_comparator(mcpwm_oper_handle_t oper);

void change_mcpwm_timer(mcpwm_oper_handle_t oper,mcpwm_timer_handle_t old_timer, mcpwm_timer_handle_t new_timer);

void set_gen_actions(mcpwm_gen_handle_t gen, mcpwm_cmpr_handle_t comparator);

void set_comp_value(mcpwm_cmpr_handle_t comparator, int compare_value);

void mcpwm_motor_test(void);