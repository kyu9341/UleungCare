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
  char pi_say;
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
  pi_say = Serial.read();
  Serial.print("pi say : ");
  Serial.print(pi_say);
  
  if (pi_say == 'a'){
    digitalWrite(ledPin, HIGH);
     Serial.print(",");
  Serial.print("LED ON");
  }
  else{
    digitalWrite(ledPin, LOW);
     Serial.print(",");
      Serial.print("LED OFF ");
  }
  Serial.print("\n");
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
