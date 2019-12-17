#include <IRremote.h>

const int RECV_PIN = 2;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop(){
  int pi_say;
  while(true){
    if(Serial.available()){ // 라즈베리파이 시리얼 값 수신
      pi_say = Serial.parseInt();
      Serial.println(pi_say);
      if(pi_say == 1){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
       delay(100);
       break;
      }
 
    
    }
    //delay(500);
  }

  while(true){
  if (irrecv.decode(&results)){

    if(results.decode_type > 0 && results.value != 0xFFFFFFFF){
          Serial.print(results.decode_type);
          Serial.print(',');
          Serial.println(results.value,HEX);
          /*
           Serial.print("decode type : ");
           Serial.println(results.decode_type);
           Serial.print("bits : ");
           Serial.println(results.bits);
           Serial.println(results.value, HEX);

         */
    }
    
    irrecv.resume();


 
    
  }
        if(Serial.available()){ // 라즈베리파이 시리얼 값 수신
    pi_say = Serial.parseInt();

    if(pi_say == 2){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
       delay(100);
       break;

    }
  }
  }
  
  digitalWrite(7,HIGH);
  delay(5000);        
  digitalWrite(7,LOW);
}
