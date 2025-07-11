// my_mcpwm.h
// This file is part of the ESP32_P4 project.
//
#include "my_mcpwm.h"

/*
老版本mcpwm在driver/mcpwm.h中,但是新版本迁移到了driver/mcpwm_prelude.h中

新版本的ESP32 设置MCPWM的方式有点麻烦： 大概就是下面的这个介绍
    (1)首先需要调用create函数创建出 timer,operator,geneartor,comparator这4个对象
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

void mcpwm_motor_test(void){
    // GPIO Init

    // 1. 定义GPIO引脚
    const int PWM_PIN   = GPIO_NUM_36;
    const int DIR_PIN   = GPIO_NUM_32;
    const int BRAKE_PIN = GPIO_NUM_25;

    // 2. 重置引脚到默认状态
    gpio_reset_pin(PWM_PIN);
    gpio_reset_pin(DIR_PIN);
    gpio_reset_pin(BRAKE_PIN);

    // 3. 设置引脚配置结构体
    gpio_config_t DIR_config = {
        .pin_bit_mask = 1ULL << DIR_PIN,
        .mode         =  GPIO_MODE_OUTPUT,
    };

    gpio_config_t BRAKE_config = {
        .pin_bit_mask = 1ULL << BRAKE_PIN,
        .mode         =  GPIO_MODE_OUTPUT,
        .pull_up_en   = GPIO_PULLUP_ENABLE    // Pull-Up Output High
    };

    // 4. 配置引脚
    gpio_config(&DIR_config);
    gpio_config(&BRAKE_config);

    // 5. 设置引脚电平
    gpio_set_level(DIR_PIN,0);
    gpio_set_level(BRAKE_PIN,1);

    
    // MCPWM INIT
    const int mcpwm_group_id      = 0;
    const int timer_resolution_hz = 1000000;    // 1Mhz表示1s输出1000000个ticks单位, 一个ticks为 1e-06 s
    const int timer_period_ticks  = 20000;      // period表示一个周期为20000个ticks单位，总时长为0.02s, 即50Hz
    const int INIT_COMP           = 8000;       // 根据tick来，取值范围从0到 period_ticks，来表示一个周期内的占空比

    // 1. Timer 定时器初始化， 定时器用来确定输出PWM的频率和PWM的周期时长
    mcpwm_timer_handle_t timer = NULL;
    mcpwm_timer_config_t timer_config = {
        .group_id = mcpwm_group_id,
        .clk_src = MCPWM_TIMER_CLK_SRC_DEFAULT,
        .resolution_hz = timer_resolution_hz,
        .period_ticks = timer_period_ticks,
        .count_mode = MCPWM_TIMER_COUNT_MODE_UP,
    };
    ESP_ERROR_CHECK(mcpwm_new_timer(&timer_config, &timer));

    // 2. Operator操作器初始化，操作器与Timer,generaotr,comparator连接
    mcpwm_oper_handle_t oper = NULL;
    mcpwm_operator_config_t operator_config = {
        .group_id = mcpwm_group_id, 
    };
    ESP_ERROR_CHECK(mcpwm_new_operator(&operator_config, &oper));

    //连接Timer
    ESP_ERROR_CHECK(mcpwm_operator_connect_timer(oper, timer));

    // 3. 比较器初始化
    mcpwm_cmpr_handle_t comparator = NULL;
    mcpwm_comparator_config_t comparator_config = {
        .flags.update_cmp_on_tez = true,
    };
    ESP_ERROR_CHECK(mcpwm_new_comparator(oper, &comparator_config, &comparator));

    // 4. 生成器初始化
    mcpwm_gen_handle_t generator = NULL;
    mcpwm_generator_config_t generator_config = {
        .gen_gpio_num = PWM_PIN,
    };

    ESP_ERROR_CHECK(mcpwm_new_generator(oper, &generator_config, &generator));

    ESP_ERROR_CHECK(mcpwm_comparator_set_compare_value(comparator, INIT_COMP));

    ESP_ERROR_CHECK(mcpwm_generator_set_action_on_timer_event(generator,
                                                            MCPWM_GEN_TIMER_EVENT_ACTION(MCPWM_TIMER_DIRECTION_UP, MCPWM_TIMER_EVENT_EMPTY, MCPWM_GEN_ACTION_LOW)));
    // go high on compare threshold
    ESP_ERROR_CHECK(mcpwm_generator_set_action_on_compare_event(generator,
                                                            MCPWM_GEN_COMPARE_EVENT_ACTION(MCPWM_TIMER_DIRECTION_UP, comparator, MCPWM_GEN_ACTION_HIGH)));

    ESP_ERROR_CHECK(mcpwm_timer_enable(timer));
    ESP_ERROR_CHECK(mcpwm_timer_start_stop(timer, MCPWM_TIMER_START_NO_STOP));

    int cmp_value = INIT_COMP;
    while(1){

        ESP_ERROR_CHECK(mcpwm_comparator_set_compare_value(comparator, cmp_value));
        vTaskDelay(pdMS_TO_TICKS(500));

        cmp_value += 1000;

        if(cmp_value == 16000){
            while(1){
                ESP_ERROR_CHECK(mcpwm_comparator_set_compare_value(comparator, cmp_value));
                vTaskDelay(pdMS_TO_TICKS(500));
                cmp_value -= 1000;

                if(cmp_value == 7000){
                    break;
                }
            }
        }
        
    }

}


