# Tarefa 2 – Programação do ESP32 (Sensor DHT22)

## Objetivo

Desenvolver e testar um código funcional para leitura de dados via sensor DHT22 conectado ao ESP32, exibindo os valores de temperatura e umidade no Monitor Serial em formato CSV.

---

## Etapas realizadas

1. **Montagem do circuito** com ESP32 e sensor DHT22 com resistor pull-up de 10kΩ entre VCC e DATA.
2. **Implementação do código** em C++ utilizando a biblioteca `DHT.h`, com leitura a cada 2 segundos.
3. **Leituras exibidas** no formato:
```
Timestamp,Temperatura,Umidade
2006,54.70,60.50
4013,54.70,45.00
...
```
4. **Testes realizados** no simulador Wokwi, com verificação da variação dos dados e validação no Serial Monitor.

---

## Conclusão

A Tarefa 2 foi executada com sucesso, validando a leitura de temperatura e umidade do sensor DHT22 via ESP32. Os dados foram coletados corretamente e estão prontos para uso na análise da Tarefa 3.
