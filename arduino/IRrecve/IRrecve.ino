#include <IRremote.h>
#include <IRremoteInt.h>

#define IRPIN 2

IRrecv ir(IRPIN);
decode_results res;

void setup() {
Serial.begin(9600);
ir.enableIRIn();    // IR 수신 시작
}

void loop() {
if (ir.decode(&res))
{
Serial.print("decode_type : ");
 Serial.print(res.decode_type);
 
Serial.print("\tvalue : ");
Serial.print(res.value, HEX);
Serial.print("\tbits : ");
Serial.println(res.bits);

ir.resume();    //  다음 값
}
}
