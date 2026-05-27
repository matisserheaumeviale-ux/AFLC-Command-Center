# Changelog

## v0.1.0

- création du projet
- ajout structure GitHub
- ajout architecture initiale
- ajout protocole AFLC-Link v1
- ajout roadmap

## v0.1.1 - AFLC-Link UART V1

### Added

- Created AFLC Command Center repository structure.
- Added STM32 Master firmware generated with STM32CubeMX.
- Added USART1 communication between PC and STM32 Master.
- Added AFLC-Link UART V1 commands:
  - `@PING?;`
  - `@STATUS?;`
  - `@ID?;`
- Added Python terminal support for:
  - `ping`
  - `status`
  - `id`
- Added serial buffer cleanup before each command.

### Validated

- PC terminal connects to COM7 at 19200 baud.
- STM32 Master answers `#PONG;`.
- STM32 Master answers `#STATUS:STM32:OK;`.
- STM32 Master answers `#ID:STM32_MASTER:AFLC_UART_V1;`.

### Notes

- Communication uses USART1, not native USB CDC.
- USART1 pins:
  - PA9 = STM32 TX
  - PA10 = STM32 RX