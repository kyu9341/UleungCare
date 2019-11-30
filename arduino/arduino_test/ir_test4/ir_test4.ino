#include <IRremote.h>

const int RECV_PIN = 7;

const int greenled = 5;
const int redled = 4;
const int yellowled = 3;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();

  pinMode(greenled, OUTPUT);
  pinMode(redled, OUTPUT);
  pinMode(yellowled, OUTPUT);
  //irrecv.blink13(true);
}

void loop(){
  
  if (irrecv.decode(&results)){
          //if(results.value < 0x0FFFFFFF){
            Serial.print("decode type");
            Serial.println(results.decode_type);
            Serial.println(results.value, HEX);


            if(results.value == 0xFFA55D){
              digitalWrite(greenled,HIGH);
              delay(500);
              digitalWrite(greenled,LOW);
            }
            else if(results.value == 0xFFA66D){
              digitalWrite(redled,HIGH);
              delay(500);
              digitalWrite(redled,LOW);
            }
            else if(results.value == 0xFFA22D){
              digitalWrite(yellowled,HIGH);
              delay(500);
              digitalWrite(yellowled,LOW);
            }
          //}
          irrecv.resume();
          
        
  }
}
