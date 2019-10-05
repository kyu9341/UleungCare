#include <IRremote.h>
 
////IR recve////////////////////////

int IRrecvPin = 2;
IRrecv irrecv(IRrecvPin);
IRsend irsend;

////////////////////////////////////////////////

//////////// sensor  //////////// 
int tmp_sensor = A0;
int light_sensor = A1;

////////////////////////////////////////////////  

const int ledPingreen = 8;
const int ledPinyellow = 9;
const int RED_PIN =7, GREEN_PIN= 6, BLUE_PIN = 5;
//const int RED_PIN =12, GREEN_PIN= 11, BLUE_PIN = 10;
void setup() {
  Serial.begin(9600);

  
  pinMode(ledPingreen, OUTPUT);
  pinMode(ledPinyellow, OUTPUT);
////IR recve////////////////////////
  irrecv.enableIRIn();  // Start the receiver
////////////////////////////////////////////////


  pinMode(RED_PIN,OUTPUT);
  pinMode(BLUE_PIN,OUTPUT);
  pinMode(GREEN_PIN,OUTPUT);


  
}


void RGB(int r, int g, int b){

  analogWrite(RED_PIN, r);
  analogWrite(GREEN_PIN, g);
  analogWrite(BLUE_PIN, b);
  
  
}

////////////////////       IR Senser          /////////////////////////////////

////////////////////       IR recive          /////////////////////////////////
void  dumpCode (decode_results *results)
{
  // Start declaration
  //Serial.print("unsigned int  ");          // variable type
  //Serial.print("rawData[");                // array name
  Serial.print(results->rawlen - 1, DEC);  // array size
  Serial.print(",");
  //Serial.print("] = {");                   // Start declaration
 
  // Dump data
  for (int i = 1;  i < results->rawlen;  i++) {
    Serial.print(results->rawbuf[i] * USECPERTICK, DEC);
    if ( i < results->rawlen-1 ) Serial.print(","); // ',' not needed on last one
    //if (!(i & 1))  Serial.print(" ");
  }
 
  // End declaration
  //Serial.print("};");  // 
 
  // Newline
  Serial.println("");
 
}


////////////////////       IR Send         /////////////////////////////////

void IR_send(int order) {
  int i;
  int khz = 38; // 38kHz carrier frequency for the NEC protocol
  unsigned int tvon[] ={4550,4500,550,1700,550,1650,550,1700,550,600,550,600,500,600,500,650,500,600,500,1750,500,1750,500,1700,550,600,500,600,550,600,500,600,500,650,500,600,500,1750,500,600,550,600,500,600,500,650,500,600,500,600,550,1700,550,600,500,1750,500,1700,550,1700,500,1750,500,1750,500,1750,500};
  unsigned int volup[] ={4500,4500,550,1700,550,1700,550,1700,550,550,550,600,500,600,550,600,500,600,550,1700,500,1750,500,1750,500,600,500,650,500,600,500,600,550,600,500,1750,500,1750,500,1700,550,600,500,600,550,600,500,600,500,650,500,600,500,600,550,600,500,1750,500,1750,500,1700,550,1700,500,1750,500};
  unsigned int voldown[] ={4500,4550,550,1650,550,1700,550,1700,550,600,500,600,550,600,500,600,550,600,500,1750,500,1700,550,1700,550,600,500,600,500,650,500,600,500,600,550,1700,500,1750,500,600,550,1700,550,600,500,600,500,650,500,600,500,600,550,600,500,1750,500,600,500,1750,500,1750,500,1750,500,1700,550};
  unsigned int chup[] ={4500,4500,550,1700,550,1700,550,1700,550,550,550,600,500,600,550,600,500,600,550,1700,500,1750,500,1750,500,600,500,650,500,600,500,600,550,600,500,600,550,1700,500,650,500,600,500,1750,500,600,550,600,500,600,500,1750,500,600,550,1700,500,1750,500,600,550,1700,550,1700,500,1750,500};
  unsigned int chdown[] ={4500,4500,550,1700,550,1700,550,1700,550,550,550,600,550,600,500,600,500,600,550,1700,550,1700,500,1750,500,600,550,600,500,600,550,600,500,600,500,650,500,600,500,600,550,600,500,1750,500,600,500,600,550,600,500,1750,500,1750,500,1700,550,1700,500,650,500,1750,500,1700,550,1700,500};
  unsigned int airon[] = {4550,4450,550,1700,600,1650,550,1700,550,550,550,600,550,550,550,550,550,600,550,1700,550,1650,550,1700,550,600,550,600,500,600,500,600,550,600,500,600,550,600,500,1750,500,600,500,600,550,600,500,600,500,650,500,1700,550,1700,550,600,500,1750,500,1700,550,1700,500,1750,500,1750,500};
  unsigned int airup[] = {4550,4500,550,1650,600,1650,550,1700,550,600,550,550,550,550,550,600,550,550,550,1700,550,1700,550,1700,550,550,550,600,500,600,550,600,500,600,550,1700,500,650,500,1700,550,600,500,600,550,600,500,600,500,650,500,600,500,1750,500,600,500,1750,500,1750,500,1750,500,1700,550,1700,550};
  unsigned int airdown[] = {4550,4500,550,1700,550,1650,550,1700,550,600,550,550,550,600,550,550,550,550,550,1700,550,1700,550,1700,550,600,500,600,550,600,500,600,500,600,550,600,500,1750,500,1750,500,600,500,600,550,600,500,600,500,650,500,1700,550,600,500,600,550,1700,500,1750,500,1750,500,1750,500,1700,550};
  
 if(order == 1)
  for(i=0;i<3;i++){
    irsend.sendRaw(tvon, sizeof(tvon) / sizeof(tvon[0]), khz); //Note the approach used to automatically calculate the size of the array.
  }
 else if(order == 2)
  for(i=0;i<3;i++){
    irsend.sendRaw(volup, sizeof(volup) / sizeof(volup[0]), khz); //Note the approach used to automatically calculate the size of the array.
  }
 else if(order == 3)
  for(i=0;i<3;i++) {
    irsend.sendRaw(voldown, sizeof(voldown) / sizeof(voldown[0]),khz ); //Note the approach used to automatically calculate the size of the array.
   }
  else if(order == 4)
  for(i=0;i<3;i++) {
    irsend.sendRaw(chup, sizeof(chup) / sizeof(chup[0]),khz ); //Note the approach used to automatically calculate the size of the array.
  }
  else if(order == 5)
  for(i=0;i<3;i++) {
    irsend.sendRaw(chdown, sizeof(chdown) / sizeof(chdown[0]),khz ); //Note the approach used to automatically calculate the size of the array.
   }

   else if(order == 6)
   for(i=0;i<3;i++){
     irsend.sendRaw(airon, sizeof(airon) / sizeof(airon[0]),khz ); //Note the approach used to automatically calculate the size of the array.
   }

   else if(order == 7)
   for(i=0;i<3;i++){
     irsend.sendRaw(airup, sizeof(airup) / sizeof(airup[0]),khz ); //Note the approach used to automatically calculate the size of the array.
   }

   else if(order == 8)
   for(i=0;i<3;i++){
     irsend.sendRaw(airdown, sizeof(airdown) / sizeof(airdown[0]),khz ); //Note the approach used to automatically calculate the size of the array.
   }
  //delay(1000); //In this example, the signal will be repeated every 5 seconds, approximately.
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////
 
void loop() {
  int i,r,g,b;
  decode_results  results;        // Somewhere to store the results
 
  int tmp = analogRead(tmp_sensor);
  int light = analogRead(light_sensor);
  int pi_say,order;
  
  //float voltage = tmp * 5000.0/1024.0; // 온도센서 값을 전압으로 변환
  //float celsius = (voltage - 500) / 10.0; // 전압을 온도로 변환
  float celsius = (5.0*tmp*100.0)/1024.0;
   
  Serial.print(celsius);
  Serial.print(",");
  Serial.print(light);
  Serial.print("\n");//send data

  
  if(Serial.available()){
    pi_say = Serial.parseInt();

    if(pi_say == 1){
       delay(100);
      r = Serial.parseInt();
      g = Serial.parseInt();
      b = Serial.parseInt();

      RGB(r,g,b);
    }
    if(pi_say == 2){
      order = Serial.parseInt();
      IR_send(order);
      //RGB(0,255,0);
      //delay(500);
      //RGB(r,g,b);
    }
    
  }
  delay(1000);

}
