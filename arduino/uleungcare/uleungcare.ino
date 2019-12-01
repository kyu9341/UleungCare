#include <IRremote.h>
 
////IR recve////////////////////////

int IRrecvPin = 2; // IR 수신 센서 포트
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

  
////////////  LED 출력 포트  //////////////////////


  pinMode(RED_PIN,OUTPUT);
  pinMode(BLUE_PIN,OUTPUT);
  pinMode(GREEN_PIN,OUTPUT);



  
}


void RGB(int r, int g, int b){ //RGB 제어 함수

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

  if(order == 1){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
       for(i=0;i<3;i++){
        irsend.sendNEC(0xFFA55D,32); //Note the approach used to automatically calculate the size of the array.
        Serial.println("send one");
        }
       delay(100);
     }
    if(order == 2){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
      for(i=0;i<3;i++){
        irsend.sendNEC(0xFFA66D,32); //Note the approach used to automatically calculate the size of the array.
        Serial.println("send two");
      }
       delay(100);
     }
    if(order == 3){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
      for(i=0;i<3;i++){
        irsend.sendNEC(0xFFA22D,32); //Note the approach used to automatically calculate the size of the array.
        Serial.println("send three");
      }
       delay(100);
     }
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

  
  if(Serial.available()){ // 라즈베리파이 시리얼 값 수신
    pi_say = Serial.parseInt();

    if(pi_say == 1){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
       delay(100);
      r = Serial.parseInt();
      g = Serial.parseInt();
      b = Serial.parseInt();

      RGB(r,g,b);
    }
    if(pi_say == 2){
      order = Serial.parseInt();
      IR_send(order);

    }
    
  }
  delay(1000);

}
