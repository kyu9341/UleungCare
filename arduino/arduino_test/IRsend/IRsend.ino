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

  Serial.begin(9600);

}

void loop() {
  int i;
  int khz = 38; // 38kHz carrier frequency for the NEC protocol
  int pi_say,order;
  //unsigned long IR_data = 0xE0E040BF;
  unsigned long IR_data = 3772793023;
  for(i=0;i<3;i++){
        irsend.sendSAMSUNG(IR_data,32); //Note the approach used to automatically calculate the size of the array.
        //irsend.sendSAMSUNG(0xE0E040BF,34); 
       
        Serial.println("send one");
        }/*
        delay(200);
  for(i=0;i<3;i++){
        irsend.sendNEC(0x20DF10EF,32);
       
        Serial.println("send one");
        }
        */
       delay(5000);
}

  
  /*
    if(Serial.available()){ // 라즈베리파이 시리얼 값 수신
    pi_say = Serial.parseInt();

    if(pi_say == 1){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
       for(i=0;i<3;i++){
        irsend.sendNEC(0xFFA55D,32); //Note the approach used to automatically calculate the size of the array.
        Serial.println("send one");
        }
       delay(100);
     }
    if(pi_say == 2){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
      for(i=0;i<3;i++){
        irsend.sendNEC(0xFFA66D,32); //Note the approach used to automatically calculate the size of the array.
        Serial.println("send two");
      }
       delay(100);
     }
    if(pi_say == 3){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
      for(i=0;i<3;i++){
        irsend.sendNEC(0xFFA22D,32); //Note the approach used to automatically calculate the size of the array.
        Serial.println("send three");
      }
       delay(100);
     }
    
  }
  */
