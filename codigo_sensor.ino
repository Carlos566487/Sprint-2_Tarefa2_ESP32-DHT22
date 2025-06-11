#include <DHT.h>  // Inclui a biblioteca responsável por lidar com sensores DHT (como o DHT22)

#define DHTPIN 4         // Define o pino do ESP32 ao qual o pino de dados do sensor está conectado
#define DHTTYPE DHT22    // Define o tipo de sensor como DHT22 (modelo digital de temperatura e umidade)

DHT dht(DHTPIN, DHTTYPE);  // Cria um objeto DHT com as configurações acima

void setup() {
  Serial.begin(115200);              // Inicializa a comunicação serial com taxa de 115200 bps
  dht.begin();                       // Inicializa o sensor DHT
  Serial.println("Timestamp,Temperatura,Umidade");  // Imprime o cabeçalho para os dados (formato CSV)
}

void loop() {
  static unsigned long startTime = millis();  // Marca o tempo inicial de execução
  delay(2000);                                // Aguarda 2 segundos entre cada leitura

  float humidity = dht.readHumidity();        // Lê o valor de umidade do sensor
  float temperature = dht.readTemperature();  // Lê o valor de temperatura em graus Celsius

  // Verifica se houve falha na leitura de algum dos dados
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Erro na leitura do sensor!");
    return; // Encerra o loop atual caso haja erro
  }

  // Imprime os dados no formato: tempo decorrido, temperatura, umidade
  Serial.print(millis() - startTime);  // Tempo decorrido desde o início
  Serial.print(",");
  Serial.print(temperature);           // Temperatura lida
  Serial.print(",");
  Serial.println(humidity);           // Umidade lida
}
