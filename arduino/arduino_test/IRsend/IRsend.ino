/*
 * IRremote: IRsendRawDemo - demonstrates sending IR codes with sendRaw
 * An IR LED must be connected to Arduino PWM pin 3.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 *
 * IRsendRawDemo - added by AnalysIR (via www.AnalysIR.com), 24 August 2015
 *
 * This example shows how to send a RAW signal using the IRremote library.
 * The example signal is actually a 32 bit NEC signal.
 * Remote Control button: LGTV Power On/Off. 
 * Hex Value: 0x20DF10EF, 32 bits
 * 
 * It is more efficient to use the sendNEC function to send NEC signals. 
 * Use of sendRaw here, serves only as an example of using the function.
 * 
 */


#include <IRremote.h>

IRsend irsend;

void setup()
{

}

void loop() {
  int i;
  int khz = 38; // 38kHz carrier frequency for the NEC protocol
  unsigned int tvon[] ={4550,4500,550,1700,550,1650,550,1700,550,600,550,600,500,600,500,650,500,600,500,1750,500,1750,500,1700,550,600,500,600,550,600,500,600,500,650,500,600,500,1750,500,600,550,600,500,600,500,650,500,600,500,600,550,1700,550,600,500,1750,500,1700,550,1700,500,1750,500,1750,500,1750,500};
  unsigned int volup[] ={4500,4500,550,1700,550,1700,550,1700,550,550,550,600,500,600,550,600,500,600,550,1700,500,1750,500,1750,500,600,500,650,500,600,500,600,550,600,500,1750,500,1750,500,1700,550,600,500,600,550,600,500,600,500,650,500,600,500,600,550,600,500,1750,500,1750,500,1700,550,1700,500,1750,500};
  unsigned int voldown[] ={4500,4550,550,1650,550,1700,550,1700,550,600,500,600,550,600,500,600,550,600,500,1750,500,1700,550,1700,550,600,500,600,500,650,500,600,500,600,550,1700,500,1750,500,600,550,1700,550,600,500,600,500,650,500,600,500,600,550,600,500,1750,500,600,500,1750,500,1750,500,1750,500,1700,550};
  unsigned int chup[] ={4500,4500,550,1700,550,1700,550,1700,550,550,550,600,500,600,550,600,500,600,550,1700,500,1750,500,1750,500,600,500,650,500,600,500,600,550,600,500,600,550,1700,500,650,500,600,500,1750,500,600,550,600,500,600,500,1750,500,600,550,1700,500,1750,500,600,550,1700,550,1700,500,1750,500};
  unsigned int chdown[] ={4500,4500,550,1700,550,1700,550,1700,550,550,550,600,550,600,500,600,500,600,550,1700,550,1700,500,1750,500,600,550,600,500,600,550,600,500,600,500,650,500,600,500,600,550,600,500,1750,500,600,500,600,550,600,500,1750,500,1750,500,1700,550,1700,500,650,500,1750,500,1700,550,1700,500};
  
 
  for(i=0;i<3;i++){
    irsend.sendSony(0xFFA25D,32); //Note the approach used to automatically calculate the size of the array.
    Serial.println("send on");
  }
  delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
  for(i=0;i<3;i++){
    irsend.sendNEC(0xFFA25D,32); //Note the approach used to automatically calculate the size of the array.
    Serial.println("send on");
  }
  delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
  for(i=0;i<3;i++){
    irsend.sendLG(0xFFA25D,32); //Note the approach used to automatically calculate the size of the array.
    Serial.println("send on");
  }
  delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
/*
  for(i=0;i<3;i++){
    irsend.sendRaw(volup, sizeof(volup) / sizeof(volup[0]), khz); //Note the approach used to automatically calculate the size of the array.
    Serial.print("send vol up\n");
  }
  delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
  for(i=0;i<3;i++) {
    irsend.sendRaw(voldown, sizeof(voldown) / sizeof(voldown[0]),khz ); //Note the approach used to automatically calculate the size of the array.
    Serial.print("send vol down\n");
   }
   delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
  for(i=0;i<3;i++) {
    irsend.sendRaw(chup, sizeof(chup) / sizeof(chup[0]),khz ); //Note the approach used to automatically calculate the size of the array.
    Serial.print("send chdup\n");
  }
  delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
  for(i=0;i<3;i++) {
    irsend.sendRaw(chdown, sizeof(chdown) / sizeof(chdown[0]),khz ); //Note the approach used to automatically calculate the size of the array.
    Serial.print("send ch down\n");
   }
  
  delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
*/
}
