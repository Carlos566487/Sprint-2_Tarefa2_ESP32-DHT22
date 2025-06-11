# Tarefa 2 – Programação do ESP32 (Sensor DHT22)

## 🎯 Objetivo

Desenvolver e testar um código funcional para leitura de dados via sensor **DHT22** conectado ao **ESP32**, exibindo valores de **temperatura** e **umidade** no Monitor Serial em formato **CSV**.

---

## 📂 Estrutura do Repositório

Nesta seção, apresentamos a organização dos arquivos do projeto, facilitando a navegação e o entendimento de cada componente.



```plaintext
Sprint-2_Tarefa2_ESP32-DHT22/
├── README.md
├── codigo/
│   └── codigo_sensor.ino
├── dados/
│   └── dados_sensor.csv
└── prints/
    └── print_serial.png
    └── grafico_dht22.png
    └── Esquema de Circuito ESP32 e DHT22.png

```

> **Descrição das pastas:**
>
> - `codigo/`: Contém o sketch Arduino (`.ino`) para leitura do DHT22.
> - `dados/`: Armazena o CSV com os dados coletados (Timestamp, Temperatura, Umidade).
> - `prints/`: Imagens demonstrando o circuito, Monitor Serial e gráficos.
> - `README.md`: Documentação do projeto.

---

## 💡 Idealização do Código

A lógica do programa foi idealizada em etapas para garantir modularidade, clareza e facilidade de manutenção. Segue diagrama representando a estrutura principal:

![Esquema de Circuito ESP32 e DHT22](prints/Esquema%20de%20Circuito%20ESP32%20e%20DHT22.png)


> **Fluxo de execução:**
>
> 1. Inicialização do sensor DHT22 e do canal Serial.
> 2. Leitura de temperatura e umidade a cada 2 segundos.
> 3. Formatação dos dados no padrão CSV (`Timestamp,Temperatura,Umidade`).
> 4. Envio dos valores ao Monitor Serial.
> 5. (Opcional) Exportação manual dos dados via Monitor Serial para análise.

---

## 🧪 Etapas Realizadas

1. **Montagem do circuito**: Conexão do DHT22 ao ESP32 com resistor pull-up de 10kΩ entre VCC e pino DATA.
2. **Implementação do código** em C++ (Arduino IDE/PlatformIO) usando a biblioteca `DHT.h`.
3. **Formato de saída**:
   ```csv
   Timestamp,Temperatura,Umidade
   2006,54.70,60.50
   4013,54.70,45.00
   ...
   ```
4. **Testes de simulação**: Validação no Wokwi e Monitor Serial, garantindo comportamento dinâmico dos dados.

---

## 📈 Visualizações e Gráficos

> **Gráfico de exemplo**: variação de temperatura e umidade ao longo do tempo.



> **Observação**: O script `grafico.py` e o arquivo `dados_sensor.csv` estão disponíveis para reproduzir ou ajustar as análises.

---

## ✅ Conclusão

A Tarefa 2 foi executada com sucesso, validando a leitura de temperatura e umidade do sensor DHT22 via ESP32. Os dados foram coletados corretamente e estão prontos para uso na análise da Tarefa 3.
---