
const int ledPingreen = 8;
const int ledPinyellow = 9;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  pinMode(ledPingreen, OUTPUT);
  pinMode(ledPinyellow, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int IR_data[150]={0};
  int i=0;

  
  digitalWrite(ledPingreen,HIGH);
  digitalWrite(ledPinyellow,LOW);
  if(Serial.available()){
    
  digitalWrite(ledPingreen,LOW);
  digitalWrite(ledPinyellow,HIGH);
    IR_data[i] = Serial.parseInt();
    //Serial.print(IR_data[i]);
    i++;
    //Serial.print("\n");
  }

  if(IR_data[i] == 0){
    for(i=0;i<150;i++){
      Serial.print(IR_data[i]);
    }
    Serial.print("\n");
    
  }
  
  

  
}
