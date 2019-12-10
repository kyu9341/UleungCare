#include <stdio.h>
#include <stdlib.h>
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);

}

void loop() {
  
 char temp[100];
 unsigned long IR_data;
  if(Serial.available()){
    byte leng = Serial.readBytesUntil('g', temp, 30);
    
    Serial.print("Input data Lenght : ");
    Serial.println(leng);

    IR_data = strtoul(temp,NULL,16);
    
    for(int i = 0; i < leng; i++){
      Serial.print(temp[i]);
    }
    Serial.println();
    Serial.println(IR_data);
  }    
/*
int IR_data=0;
  if(Serial.available()){
    IR_data = Serial.parseInt();

    Serial.println(IR_data);
  }
  */
  
}
