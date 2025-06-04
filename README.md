# Compito - Analizzatore IP con Tkinter

Questa è una semplice applicazione GUI sviluppata in Python usando la libreria `tkinter`. Permette di inserire manualmente un indirizzo IP (diviso in 4 ottetti) e di eseguire alcune operazioni su di esso, come il controllo della validità, la determinazione della classe, subnet mask, CIDR, wildcard e il calcolo del gateway.

## Caratteristiche

- **Controllo IP**: Verifica che ogni ottetto sia compreso tra 0 e 255.
- **Classe IP, Subnet Mask e CIDR**:
  - Determina se l'indirizzo IP è di classe A, B, C o D.
  - Mostra la subnet mask e la notazione CIDR corrispondente.
  - Calcola l'indirizzo di rete.
- **Wildcard e Broadcast**:
  - Calcola la wildcard mask in base alla classe IP.
  - Mostra l'indirizzo di broadcast teorico.
- **Gateway**:
  - Suggerisce un gateway standard per la rete.

## Requisiti

- Python 3.x

Non sono richieste librerie esterne. Tutto è basato sulla libreria standard `tkinter`.

## Utilizzo

1. Esegui lo script Python:

```bash
python IPCalculator.py
