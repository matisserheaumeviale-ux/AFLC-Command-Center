# Project ID

## Nom
AFLC Command Center

## Nom court
AFLC-CC

## Version
v0.1.0

## Type
Projet embarqué multi-cartes avec logiciel PC.

## But
Créer une plateforme AFLC avec STM32, PIC16F88, logiciel PC, protocole série maison, PWM fan, lecture RPM et sécurité indépendante.

## Modules principaux

| Module | Rôle |
|---|---|
| STM32 Master | Cerveau principal |
| STM32 Fan Node | PWM fan + RPM |
| PIC16F88 Safety Node | Sécurité indépendante |
| PC Software | Dashboard + logs |
| NI Instrument | Validation labo |

## Langages

- C pour STM32
- C / Assembleur pour PIC16F88
- Python pour logiciel PC
- Markdown pour documentation

## Protocoles

- UART PC ↔ STM32
- UART STM32 ↔ PIC16F88
- AFLC-Link v1