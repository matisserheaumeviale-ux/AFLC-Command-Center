# STM32 Master Pinout

## MCU

STM32F103CBT6

## Communication PC

| Pin | Fonction |
|---|---|
| PA9 | USART1_TX |
| PA10 | USART1_RX |

USART1 : 19200 baud, 8N1

## Communication PIC16F88 Safety Node

| Pin | Fonction |
|---|---|
| PA2 | USART2_TX |
| PA3 | USART2_RX |

USART2 : 19200 baud, 8N1

## Communication STM32 Fan Node

| Pin | Fonction |
|---|---|
| PB6 | I2C1_SCL |
| PB7 | I2C1_SDA |

I2C1 : 100 kHz, 7-bit addressing

## Status LED

| Pin | Fonction |
|---|---|
| PC13 | LED_STATUS |

## Debug

| Pin | Fonction |
|---|---|
| PA13 | SWDIO |
| PA14 | SWCLK |

## Pins réservées fan futures

| Pin | Fonction future |
|---|---|
| PA6 | FAN1_PWM |
| PA7 | FAN2_PWM |
| PB0 | FAN3_PWM |
| PB1 | FAN4_PWM |
| PA0 | FAN1_TACH |
| PA1 | FAN2_TACH |
| PB8 | FAN3_TACH |
| PB9 | FAN4_TACH |