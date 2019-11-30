#include <IRremote.h>

const int RECV_PIN = 7;

IRrecv irrecv(RECV_PIN);
decode_results results;
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 
  irrecv.enableIRIn();

}

void loop() {
  // put your main code here, to run repeatedly:
if (irrecv.decode(&results)){
   //Serial.println("get data");
    if(results.decode_type != -1 && results.decode_type != 0){
      Serial.print(results.decode_type);
      Serial.print(',');
      Serial.println(results.value, HEX);
    }
    
  irrecv.resume();
          
  }

  
}
