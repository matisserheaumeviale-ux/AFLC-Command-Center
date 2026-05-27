# Hardware

## Cartes

- STM32 Master
- STM32 Fan Node
- PIC16F88 Safety Node
- PC
- NI Instrument

## Connexions

| Connexion | Type |
|---|---|
| PC ↔ STM32 Master | USB/UART |
| STM32 Master ↔ PIC16F88 | UART |
| STM32 Master ↔ STM32 Fan Node | UART/I2C/CAN |
| STM32 Fan Node ↔ Fan | PWM + Tach |
| NI ↔ Signaux | mesure |

## Attention niveaux logiques

STM32 : 3.3 V  
PIC16F88 : souvent 5 V

À prévoir :

- GND commun
- protection entrée RX STM32 si PIC en 5 V
- diviseur de tension ou level shifter
PC Terminal
  |
  | USART1 19200
  | PA9/PA10
  v
STM32 Master
  |
  | USART2 19200
  | PA2/PA3
  v
PIC16F88 Safety Node

STM32 Master
  |
  | I2C1 100 kHz
  | PB6/PB7
  v
STM32 Fan Node