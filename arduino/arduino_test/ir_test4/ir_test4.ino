#include <IRremote.h>

const int RECV_PIN = 7;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
  //irrecv.blink13(true);
}

void loop(){
  if (irrecv.decode(&results)){
          if(results.value < 0x0FFFFFFF){
            Serial.print("decode type");
            Serial.println(results.decode_type);
            Serial.println(results.value, HEX);
          }
          irrecv.resume();
          
        
  }
}
