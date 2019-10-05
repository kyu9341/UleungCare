#include <IRremote.h>
 
////IR recve////////////////////////

int IRrecvPin = 2;
IRrecv irrecv(IRrecvPin);

////////////////////////////////////////////////

//////////// sensor  //////////// 
int tmp_sensor = A0;
int light_sensor = A1;

////////////////////////////////////////////////  

const int ledPingreen = 8;
const int ledPinyellow = 9;
const int RED_PIN =4, GREEN_PIN= 3, BLUE_PIN = 2;

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

void loop() {
  int i,r,g,b;
  decode_results  results;        // Somewhere to store the results
 
  int tmp = analogRead(tmp_sensor);
  int light = analogRead(light_sensor);
  int pi_say;
  
  //float voltage = tmp * 5000.0/1024.0; // 온도센서 값을 전압으로 변환
  //float celsius = (voltage - 500) / 10.0; // 전압을 온도로 변환
  float celsius = (5.0*tmp*100.0)/1024.0;
   
  Serial.print(celsius);
  Serial.print(",");
  Serial.print(light);
  Serial.print("\n");//send data

  
  if(Serial.available()){
    pi_say = Serial.parseInt();
    if(pi_say <0 || pi_say>20)
      digitalWrite(ledPingreen, HIGH);
      
    /*
    if(pi_say == 1)
      RGB(255,0,255);
     else if(pi_say == 2)
      RGB(0,255,255);
     else if(pi_say == 3)
      RGB(255,255,0);
     */

    if(pi_say == 1){
       //delay(100);
      r = Serial.parseInt();
      g = Serial.parseInt();
      b = Serial.parseInt();

      RGB(r,g,b);
    }
    
  }
  delay(1000);

}

void RGB(int r, int g, int b){

  analogWrite(RED_PIN, r);
  analogWrite(GREEN_PIN, g);
  analogWrite(BLUE_PIN, b);
  
  
}

////////////////////       IR Senser          /////////////////////////////////
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
 
