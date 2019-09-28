int tmp_sensor = A0;
int light_sensor = A1;
const int ledPin = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  int tmp = analogRead(tmp_sensor);
  int light = analogRead(light_sensor);

  float voltage = tmp * 5000.0/1024.0; // 온도센서 값을 전압으로 변환
  float celsius = (voltage - 500) / 10.0; // 전압을 온도로 변환

  //Serial.print(celsius);
  //Serial.print(" C\n");

  //Serial.print(light);
  //Serial.print(" b\n");

  Serial.print(celsius);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.print("pi say : ");
  Serial.print(Serial.read());
  Serial.print("\n");
  if (Serial.read() == 'a'){
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
  delay(1000);

}

void flash(int n)
{
  for (int i = 0; i < n; i++)
  {
    digitalWrite(ledPin, HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
  }
}
