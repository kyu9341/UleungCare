#include <IRremote.h>

IRsend irsend;

void setup()
{
  Serial.begin(9600);
}

void loop() {
    //for (int i = 0; i < 3; i++) {
      irsend.sendNEC(0x20DF10EF, 32); // Sony TV power code

      Serial.print("send\n");
      delay(40);
    //}
  
}
