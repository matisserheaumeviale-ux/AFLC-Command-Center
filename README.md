# AFLC Command Center

AFLC Command Center est un projet embarqué multi-cartes basé sur STM32, PIC16F88 et un logiciel PC.

Le but est de créer un système de contrôle de ventilateurs intelligent avec communication série, protocole maison, PWM, lecture RPM, sécurité indépendante et instrumentation de laboratoire.

## Objectif principal

Créer un système AFLC où :

- le PC sert d’interface de contrôle
- le STM32 Master fait les calculs et décisions
- le STM32 Fan Node contrôle les ventilateurs
- le PIC16F88 agit comme module de sécurité
- les instruments NI servent à valider les signaux

## Architecture globale

```text
PC Software
    ↓ USB/UART
STM32 Master
    ↓ UART/I2C/CAN
STM32 Fan Node
    ↓
Fan PWM + Tach

STM32 Master
    ↓ UART
PIC16F88 Safety Node

NI Instrument
    ↓
Validation PWM / RPM / courant / tension
