// my_mcpwm.h
// This file is part of the ESP32_P4 project.
//
#include "my_mcpwm.h"

/*
老版本mcpwm在driver/mcpwm.h中,但是新版本迁移到了driver/mcpwm_prelude.h中

新版本的ESP32 设置MCPWM的方式有点麻烦： 大概就是下面的这个介绍
    (1)首先需要调用create函数创建出 group,timer,operator,geneartor,comparator这5个对象
    (2)group对象负责管理MCPWM的硬件资源组，一般ESP常见有两个MCPWM组 所以group_id可以选择0或者1
    (3)timer对象负责定时器的配置，比如计数模式，频率等等常见参数 定时器的决定了PWM输出的频率，频率越高,实时控制分辨率就高
    (4)operator对象负责输出通道的配置,通常一个MCPWM硬件资源组有两个输出通道(A/B)
    (5)generator对象负责将信号绑定到引脚上

    解释：可以把Timer看作是信号源, group,opeartor,geneartor可以看作是信号通路
          PWM信号从Timer发出，经过group_id的group的operator上，最终到达opeartor绑定的GPIO引脚

    创建好了之后， 要开始进行连接
    (6)连接operator和timer，timer在信号输出最后口充当着把门和控制输出频率的存在
    (7)连接generator和opeartor，导通信号传输通道

    (8)Comparator对象负责PWM信号的占空比， comparator需要连接到opeartor上
    比较器就是当计数没有达到比较器的值时，会一直输出高电平，当计数达到比较器的值时，输出低电平
    所以比较值直接决定了输出的PWM占空比

    (9)设置generator的行为，通常是周期开始时输出高电平，比较值时输出低电平
    (10)启动timer

*/


mcpwm_timer_handle_t create_mcpwm_timer(int mcpwm_group_id,int resolution_hz, int period_ticks)
{
    mcpwm_timer_handle_t timer         = NULL;
    mcpwm_timer_config_t timer_config  = {
        .group_id      = mcpwm_group_id,
        .clk_src       = MCPWM_TIMER_CLK_SRC_DEFAULT, 
        .resolution_hz = resolution_hz,      // 1s有100W个ticks, 一个tick为1us
        .count_mode    = MCPWM_TIMER_COUNT_MODE_UP,
        .period_ticks  = period_ticks         // 以ticks作为单位， 这里时20000个ticks, 也就是20ms一个周期
    }; 
    ESP_ERROR_CHECK(mcpwm_new_timer(&timer_config, &timer));
    return timer;
}

mcpwm_oper_handle_t create_mcpwm_operator(int mcpwm_group_id, mcpwm_timer_handle_t timer)
{
    mcpwm_oper_handle_t oper          = NULL;
    mcpwm_operator_config_t oper_config   = {
        .group_id = mcpwm_group_id
    };
    ESP_ERROR_CHECK(mcpwm_new_operator(&oper_config, &oper));
    ESP_ERROR_CHECK(mcpwm_operator_connect_timer(oper, timer));
    return oper;
}

mcpwm_gen_handle_t create_mcpwm_generator(mcpwm_oper_handle_t oper, gpio_num_t pwm_gpio_num)
{
    mcpwm_gen_handle_t gen       = NULL;
    mcpwm_generator_config_t gen_config = {
        .gen_gpio_num = pwm_gpio_num,
        .flags = { .invert_pwm = true }
    };
    ESP_ERROR_CHECK(mcpwm_new_generator(oper, &gen_config, &gen));
    return gen;
}

mcpwm_cmpr_handle_t create_mcpwm_comparator(mcpwm_oper_handle_t oper)
{
    mcpwm_cmpr_handle_t comparator = NULL;
    mcpwm_comparator_config_t cmpr_config = {
        .flags = { 0 }
    };
    ESP_ERROR_CHECK(mcpwm_new_comparator(oper, &cmpr_config, &comparator));
    return comparator;
}

void change_mcpwm_timer(mcpwm_oper_handle_t oper,mcpwm_timer_handle_t old_timer, mcpwm_timer_handle_t new_timer)
{
    //释放旧定时器
    mcpwm_timer_start_stop(old_timer, MCPWM_TIMER_STOP_FULL);
    mcpwm_timer_disable(old_timer);
    mcpwm_del_timer(old_timer);
    //连接新定时器
    ESP_ERROR_CHECK(mcpwm_operator_connect_timer(oper, new_timer));
    //启动新定时器
    mcpwm_timer_enable(new_timer);
    ESP_ERROR_CHECK(mcpwm_timer_start_stop(new_timer,MCPWM_TIMER_START_NO_STOP));
}

void set_gen_actions(mcpwm_gen_handle_t gen, mcpwm_cmpr_handle_t comparator)
{
    // 设置generator的行为
    mcpwm_gen_timer_event_action_t action_on_timer = {
        .direction = MCPWM_TIMER_DIRECTION_UP,
        .event = MCPWM_TIMER_EVENT_EMPTY, // 计数器归零（周期开始）
        .action = MCPWM_GEN_ACTION_HIGH   // 输出高电平
    };
    ESP_ERROR_CHECK(mcpwm_generator_set_action_on_timer_event(gen, action_on_timer));

    // 设置比较器的行为
    mcpwm_gen_compare_event_action_t action_on_compare = {
        .direction = MCPWM_TIMER_DIRECTION_UP,
        .comparator = comparator,
        .action = MCPWM_GEN_ACTION_LOW // 输出低电平
    };
    ESP_ERROR_CHECK(mcpwm_generator_set_action_on_compare_event(gen, action_on_compare));

}

void set_comp_value(mcpwm_cmpr_handle_t comparator, int compare_value)
{
    // 设置比较器的比较值
    ESP_ERROR_CHECK(mcpwm_comparator_set_compare_value(comparator, compare_value));
}

void mcpwm_motor_test(void){

    int mcpwm_group_id      = 0;
    int timer_resolution_hz = 1000000; 
    int timer_period_ticks  = 20000;
    int comp_value          = 100000; 

    mcpwm_timer_handle_t timer   = create_mcpwm_timer(mcpwm_group_id, timer_resolution_hz, timer_period_ticks);
    mcpwm_oper_handle_t oper     = create_mcpwm_operator(mcpwm_group_id, timer);
    mcpwm_gen_handle_t gen       = create_mcpwm_generator(oper, PWM_PIN);
    mcpwm_cmpr_handle_t comparator = create_mcpwm_comparator(oper);
    set_gen_actions(gen, comparator);
    mcpwm_timer_enable(timer);
    ESP_ERROR_CHECK(mcpwm_timer_start_stop(timer,MCPWM_TIMER_START_NO_STOP));

    ESP_LOGI("MCPWM", "PWM started on GPIO %d", PWM_PIN);

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

    gpio_set_level(DIR_PIN, 1);

    while(1){
        
        set_comp_value(comparator, comp_value);    // 10%
        vTaskDelay(1000/portTICK_PERIOD_MS);       // (1000/portTICK_PERIOD_MS)是1000ms
        set_comp_value(comparator, comp_value*2);  // 20%
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*3);  // 30%
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*4);  // 40%
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*5);  // 50%
        vTaskDelay(1000/portTICK_PERIOD_MS);
        gpio_set_level(DIR_PIN,0);                 // 反向
        set_comp_value(comparator, comp_value*5); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*4); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*3); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*2); 
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*1);
        vTaskDelay(1000/portTICK_PERIOD_MS);
        set_comp_value(comparator, comp_value*5);  // 50%
        gpio_set_level(BRAKE_PIN,1);               // 急刹
       
    }
}



