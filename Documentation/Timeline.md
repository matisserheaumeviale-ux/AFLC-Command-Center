````md
# AFLC Command Center — Timeline / Development Roadmap

Version: 0.1  
Project Status: Active Development  
Main MCU: STM32F103CBT6  
Secondary MCU: PIC16F88  
Communication Standard: AFLC-Link UART V1  

---

# Global Vision

The AFLC Command Center project aims to create a modular intelligent fan-control ecosystem using multiple microcontrollers, PC software, custom communication protocols, telemetry, monitoring, and safety systems.

The architecture is separated into multiple nodes:

| Node | Role |
|---|---|
| STM32 Master | Main controller and protocol manager |
| PIC16F88 Safety Node | Independent safety monitoring |
| STM32 Fan Node | PWM and RPM fan management |
| PC Software | Monitoring, commands, telemetry, GUI |
| Future NI Instrumentation | Sensor acquisition and diagnostics |

---

# Current Architecture

```text
PC Software
    ↓ UART / USB Serial
STM32 Master
    ↓ USART2
PIC16F88 Safety Node

Future:
STM32 Master
    ↓ I2C / UART / AFLC-Link
STM32 Fan Nodes
````

---

# Phase 0 — Repository Initialization

Status: COMPLETE

## Goals

* Create clean project structure
* Initialize GitHub repository
* Define documentation standards
* Create AFLC-Link protocol base

## Completed

* GitHub repository created
* Main project folders created
* STM32 firmware project generated
* Python terminal created
* Initial protocol documentation created
* Build system validated
* VSCode QC1 extension validated

## Deliverables

| Deliverable          | Status |
| -------------------- | ------ |
| Repository           | DONE   |
| README               | DONE   |
| CHANGELOG            | DONE   |
| ROADMAP              | DONE   |
| Protocol folder      | DONE   |
| STM32 CubeMX project | DONE   |
| Makefile build       | DONE   |

---

# Phase 1 — STM32 Master UART Validation

Status: COMPLETE

## Objective

Validate reliable UART communication between PC software and STM32 Master.

## Hardware

| Component | Value         |
| --------- | ------------- |
| MCU       | STM32F103CBT6 |
| UART      | USART1        |
| Baudrate  | 19200         |
| TX        | PA9           |
| RX        | PA10          |
| Debug     | ST-Link V2    |

## Communication Chain

```text
PC Software
↓
COM7
↓
ST-Link VCP / USB-Serial
↓
USART1
↓
STM32 Master
```

## Commands Implemented

| Command | TX Message | RX Message                     |
| ------- | ---------- | ------------------------------ |
| ping    | @PING?;    | #PONG;                         |
| status  | @STATUS?;  | #STATUS:STM32:OK;              |
| id      | @ID?;      | #ID:STM32_MASTER:AFLC_UART_V1; |

## Features Completed

* UART initialization
* RX buffer parser
* Command parser
* Python serial terminal
* COM auto-detection
* Buffer cleanup
* Response validation
* Error handling

## Validation Results

| Test                | Result |
| ------------------- | ------ |
| Build               | PASS   |
| Flash               | PASS   |
| UART RX             | PASS   |
| UART TX             | PASS   |
| Ping protocol       | PASS   |
| Status protocol     | PASS   |
| ID protocol         | PASS   |
| Long-term stability | PASS   |

---

# Phase 2 — AFLC-Link Protocol Core

Status: IN PROGRESS

## Objective

Create standardized protocol system for all AFLC devices.

## Planned Features

| Feature            | Status      |
| ------------------ | ----------- |
| Packet structure   | IN PROGRESS |
| CRC validation     | TODO        |
| Device addressing  | TODO        |
| Multi-node support | TODO        |
| Error codes        | TODO        |
| Heartbeat system   | TODO        |
| Auto-discovery     | TODO        |

## Planned Message Format

```text
@DEVICE:COMMAND:VALUE;
```

Example:

```text
@FAN1:PWM:65;
@PIC:SAFE?;
@MASTER:STATUS?;
```

## Planned Responses

```text
#OK;
#ERR:BAD_CMD;
#FAN1:RPM:1200;
```

---

# Phase 3 — PIC16F88 Safety Node

Status: NEXT

## Objective

Add an independent hardware safety controller.

## Safety Responsibilities

| Function               | Description                  |
| ---------------------- | ---------------------------- |
| Fan failure detection  | Detect stalled fan           |
| Overtemperature        | Detect critical temperatures |
| Emergency shutdown     | Force safe state             |
| PWM fallback           | Safe PWM mode                |
| Communication watchdog | Detect STM32 failure         |

## Communication

| Parameter  | Value    |
| ---------- | -------- |
| Link       | USART2   |
| Master MCU | STM32    |
| Safety MCU | PIC16F88 |

## Planned Commands

| Command      | Purpose            |
| ------------ | ------------------ |
| @PIC:SAFE?;  | Safety status      |
| @PIC:TEMP?;  | Safety temperature |
| @PIC:FAULT?; | Fault flags        |
| @PIC:RESET;  | Reset safety node  |

## Planned Responses

```text
#PIC:SAFE:OK;
#PIC:TEMP:42;
#PIC:FAULT:NONE;
```

## Hardware Tasks

* Configure USART2
* Configure PIC UART
* Implement parser on PIC
* Implement watchdog
* Add fault LEDs

---

# Phase 4 — STM32 Fan Node

Status: PLANNED

## Objective

Offload PWM and tachometer management to dedicated STM32 nodes.

## Planned Features

| Feature             | Description           |
| ------------------- | --------------------- |
| 25 kHz PWM          | Standard PC fan PWM   |
| RPM measurement     | Tach capture          |
| Fan auto-detection  | Detect connected fans |
| Independent control | Per-fan PWM           |
| Telemetry           | RPM + fault reporting |

## Planned Hardware

| Signal   | STM32 Pin |
| -------- | --------- |
| FAN1_PWM | PA6       |
| FAN2_PWM | PA7       |
| FAN3_PWM | PB0       |
| FAN4_PWM | PB1       |

## Planned Tach Inputs

| Signal    | STM32 Pin |
| --------- | --------- |
| FAN1_TACH | PA0       |
| FAN2_TACH | PA1       |
| FAN3_TACH | PA2       |
| FAN4_TACH | PA3       |

## Planned Commands

```text
@FAN1:PWM:75;
@FAN1:RPM?;
@FAN2:STOP;
```

---

# Phase 5 — PC Software Expansion

Status: PLANNED

## Objective

Transform Python terminal into complete AFLC desktop software.

## Planned Features

| Feature            | Status |
| ------------------ | ------ |
| GUI dashboard      | TODO   |
| Live telemetry     | TODO   |
| RPM graphs         | TODO   |
| Temperature graphs | TODO   |
| Logging            | TODO   |
| Config profiles    | TODO   |
| Firmware updater   | TODO   |
| Auto-connect       | TODO   |

## Planned Technologies

| Technology   | Purpose        |
| ------------ | -------------- |
| Python       | Backend        |
| PySide6 / Qt | GUI            |
| pyserial     | UART           |
| matplotlib   | Graphs         |
| JSON         | Config storage |

---

# Phase 6 — AFLC Hardware Platform

Status: PLANNED

## Objective

Create complete custom AFLC PCB ecosystem.

## Planned Features

| Feature             | Description            |
| ------------------- | ---------------------- |
| PCIe power input    | High current fans      |
| USB internal header | PC communication       |
| TVS protection      | ESD protection         |
| Polyfuses           | Overcurrent protection |
| Buck converters     | 12V → 5V → 3.3V        |
| Status LEDs         | Diagnostics            |
| LCD support         | Local display          |

---

# Phase 7 — Intelligent Control System

Status: FUTURE

## Objective

Add advanced optimization and autonomous control.

## Planned Features

| Feature            | Description           |
| ------------------ | --------------------- |
| Thermal prediction | Predict heat spikes   |
| AI fan curves      | Dynamic optimization  |
| Sensor fusion      | Multi-sensor analysis |
| Adaptive acoustics | Noise optimization    |
| Failure prediction | Predict fan wear      |

---

# Phase 8 — AFLC Network Ecosystem

Status: FUTURE

## Objective

Support multiple synchronized AFLC boards.

## Planned Features

| Feature             | Description              |
| ------------------- | ------------------------ |
| Multi-board sync    | Shared telemetry         |
| AFLC-Link bus       | Inter-node communication |
| Distributed control | Multiple controllers     |
| Global monitoring   | Unified dashboard        |

---

# Current Priorities

| Priority | Task                           |
| -------- | ------------------------------ |
| P0       | Stabilize UART parser          |
| P0       | Add PIC16F88 communication     |
| P1       | Add PWM fan control            |
| P1       | Add tachometer capture         |
| P2       | Add GUI dashboard              |
| P2       | Add telemetry logging          |
| P3       | Add advanced protocol features |

---

# Current Working State

| Subsystem          | Status          |
| ------------------ | --------------- |
| STM32 build        | WORKING         |
| UART communication | WORKING         |
| Python terminal    | WORKING         |
| AFLC-Link V1       | WORKING         |
| PIC16F88 link      | NOT IMPLEMENTED |
| PWM control        | NOT IMPLEMENTED |
| Fan telemetry      | NOT IMPLEMENTED |
| GUI                | NOT IMPLEMENTED |

---

# Current Validated Commands

```text
ping
status
id
```

## Responses

```text
#PONG;
#STATUS:STM32:OK;
#ID:STM32_MASTER:AFLC_UART_V1;
```

```
```
