#include <IRremote.h>

const int RECV_PIN = 2;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop(){


  if (irrecv.decode(&results)){

    //if(results.decode_type > 0 && results.value != 0xFFFFFFFF){
          Serial.print(results.decode_type);
          Serial.print(',');
          Serial.println(results.value,HEX);
    //}
    
    irrecv.resume();
    
  }
}
