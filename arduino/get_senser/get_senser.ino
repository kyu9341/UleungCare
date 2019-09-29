int tmp_sensor = A0;
int light_sensor = A1;
const int ledPingreen = 8;
const int ledPinyellow = 9;
const int RED_PIN =12, GREEN_PIN= 11, BLUE_PIN = 10;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPingreen, OUTPUT);

  pinMode(ledPinyellow, OUTPUT);

  pinMode(RED_PIN,OUTPUT);
  pinMode(BLUE_PIN,OUTPUT);
  pinMode(GREEN_PIN,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  int tmp = analogRead(tmp_sensor);
  int light = analogRead(light_sensor);
  char pi_say = Serial.read();
  float voltage = tmp * 5000.0/1024.0; // 온도센서 값을 전압으로 변환
  float celsius = (voltage - 500) / 10.0; // 전압을 온도로 변환
  
   
  Serial.print(celsius);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.print(pi_say);
  Serial.print("\n");

  if(pi_say == 'a'){
    digitalWrite(ledPingreen,HIGH);
    digitalWrite(ledPinyellow,LOW);
    RGB(0,0,0);
  }
  else if(pi_say == 'b'){
    digitalWrite(ledPinyellow,HIGH);
    digitalWrite(ledPingreen,LOW);
    RGB(0,0,0);
  }
  else{
    digitalWrite(ledPingreen,LOW);
    digitalWrite(ledPinyellow,LOW);
    RGB(255,0,0);
  }
  delay(1000);

}

void RGB(int r, int g, int b){

  analogWrite(RED_PIN, r);
  analogWrite(BLUE_PIN, g);
  analogWrite(GREEN_PIN, b);
  
  
}
