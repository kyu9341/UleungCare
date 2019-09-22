
int tmp36 = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  int sensor = analogRead(tmp36);

  float voltage = sensor * 5000.0/1024.0; // 온도센서 값을 전압으로 변환
  float celsius = (voltage - 500) / 10.0; // 전압을 온도로 변환

  Serial.print(celsius);
  Serial.print(" C\n");
  delay(1000);

}
