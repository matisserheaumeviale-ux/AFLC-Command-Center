# Architecture

## Vue globale

```text
PC Software
    ↓ USB/UART
STM32 Master
    ↓ UART
STM32 Fan Node
    ↓ PWM / Tach
Fan 4-pin

STM32 Master
    ↓ UART
PIC16F88 Safety Node
STM32 Master

Rôle :

recevoir les commandes du PC
calculer la logique AFLC
envoyer les consignes aux nodes
superviser les erreurs
gérer les modes AUTO / MANUAL / SAFE
STM32 Fan Node

Rôle :

générer le PWM fan
lire le tach/RPM
envoyer télémétrie au Master
appliquer les consignes reçues
PIC16F88 Safety Node

Rôle :

surveiller que le STM32 est vivant
détecter timeout communication
activer failsafe
contrôler LED erreur / buzzer
forcer fan 100 % si panne
PC Software

Rôle :

envoyer commandes
afficher status
logger données CSV
afficher graphiques
tester protocole

---

## `PROTOCOL.md`

```md
# AFLC-Link v1

## But

AFLC-Link est le protocole série utilisé pour faire communiquer le PC, le STM32 Master, le STM32 Fan Node et le PIC16F88.

## Format commande

```text
@MODULE:COMMANDE:VALEUR;
Format réponse
#MODULE:REPONSE:VALEUR;
Symboles
Symbole	Rôle
@	Début d’une commande
#	Début d’une réponse
:	Séparateur
;	Fin du message
?	Question / lecture
Exemples
@PING?;
#PONG;

@STATUS?;
#STATUS:OK;

@FAN1:PWM:65;
#FAN1:OK:65;

@FAN1:RPM?;
#FAN1:RPM:1480;

@PIC:SAFE?;
#PIC:SAFE:OK;
Erreurs
#ERR:BAD_CMD;
#ERR:BAD_VALUE;
#ERR:TIMEOUT;
#ERR:UNKNOWN_NODE;

---

## `ROADMAP.md`

```md
# Roadmap

## Phase 0 — GitHub

- créer repo
- créer arborescence
- ajouter README
- ajouter documentation de base

## Phase 1 — Protocole

- définir AFLC-Link v1
- définir commandes
- définir réponses
- définir erreurs

## Phase 2 — PC Terminal

- créer terminal Python
- détecter port série
- envoyer commandes
- lire réponses
- logger CSV

## Phase 3 — STM32 Master

- recevoir commandes PC
- parser protocole
- répondre au PC
- envoyer commandes au PIC
- envoyer commandes au Fan Node

## Phase 4 — PIC16F88 Safety Node

- recevoir commandes UART
- répondre au STM32
- détecter timeout
- activer failsafe
- contrôler LED/buzzer

## Phase 5 — STM32 Fan Node

- générer PWM fan
- lire RPM
- envoyer status
- appliquer consignes

## Phase 6 — Dashboard PC

- interface graphique
- affichage RPM/PWM/température
- boutons contrôle
- graphiques live

## Phase 7 — Validation NI

- mesurer PWM
- mesurer tach
- mesurer courant
- comparer valeurs NI vs STM32