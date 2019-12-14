#include <IRremote.h>
 
////IR recve////////////////////////

int IRrecvPin = 2; // IR 수신 센서 포트
IRrecv irrecv(IRrecvPin);
IRsend irsend; 
decode_results  results;        // Somewhere to store the results
////////////////////////////////////////////////

//////////// sensor  //////////// 
int tmp_sensor = A0;
int light_sensor = A1;

////////////////////////////////////////////////  

const int ledPingreen = 8;
const int ledPinyellow = 9;
const int RED_PIN =6, GREEN_PIN= 9, BLUE_PIN = 10;
//const int RED_PIN =12, GREEN_PIN= 11, BLUE_PIN = 10;
void setup() {
  Serial.begin(9600);

  
  pinMode(ledPingreen, OUTPUT);
  pinMode(ledPinyellow, OUTPUT);
  
////IR recve////////////////////////
  //irrecv.enableIRIn();  // Start the receiver

  
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

////////////////////       IR send          /////////////////////////////////
void  IR_send(int decode_type,unsigned long IR_data ){

  int i;
  int khz = 38;
  RGB(0,255,0);
  for(i=0;i<3;i++){
    irsend.sendSAMSUNG(IR_data,32);
  }
  
 }


////////////////////       IR recive         /////////////////////////////////

void regist_IR() {
  int pi_say;
  int count = 0;
  while(true){
    //Serial.println("wait remote data");
    if (irrecv.decode(&results)){

      if(results.decode_type > 0 && results.value != 0xFFFFFFFF){
        RGB(0,0,0);
        Serial.print(results.decode_type);
        Serial.print(',');
        Serial.println(results.value,HEX);
        count++;
        delay(100);
        RGB(255,0,0);
          /*
           Serial.print("decode type : ");
           Serial.println(results.decode_type);
           Serial.print("bits : ");
           Serial.println(results.bits);
           Serial.println(results.value, HEX);

         */
      }
    
      irrecv.resume();

    }
    
    if(Serial.available()){ // 라즈베리파이 시리얼 값 수신
                            // 기존에는 라즈베리파이에서 2를 받아서 종료하려고 했으나 받지를 못함
      pi_say = Serial.parseInt();

      if(pi_say == 2){ // 리모컨 등록 절차 종료 
       //delay(100);
       irrecv.resume();
       break;

      }
    }
    //if(count >20){// 20번 진행시 종료
    //  break;
    //}
    
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////
 
void loop() {
  int i,r,g,b;
  int decode_type;
  int tmp = analogRead(tmp_sensor);
  int light = analogRead(light_sensor);
  int pi_say,order;
  char pi_say_arr[100];
  float voltage = tmp * 5000.0/1024.0; // 온도센서 값을 전압으로 변환
  float celsius = (voltage - 500) / 10.0; // 전압을 온도로 변환
  //float celsius = (5.0*tmp*100.0)/1024.0;
  unsigned long IR_data; 

  if(Serial.available()){ // 라즈베리파이 시리얼 값 수신
    pi_say = Serial.parseInt();

    if(pi_say == 3){//home data 읽기
        Serial.print(celsius);
        Serial.print(",");
        Serial.println(light);
        
        //Serial.print("\n");//send data
    }
    
    if(pi_say == 1){ // 라즈베리파이 시리얼 통신 값에 따른 아두이노 제어 
       //delay(100);
      r = Serial.parseInt();
      g = Serial.parseInt();
      b = Serial.parseInt();

      RGB(r,g,b);
    }
    if(pi_say == 2){  // 리모컨값 등록 절차 시작
       RGB(255,0,0);
       irrecv.enableIRIn();  // Start the receiver 기존 setup에서 진행 했지만 오류로 인해 다시 해줌
       regist_IR();
       RGB(0,255,0);
    }
    if(pi_say == 4){
      decode_type = Serial.parseInt();
      byte leng = Serial.readBytesUntil('g', pi_say_arr, 30);
      IR_data = strtoul(pi_say_arr,NULL,16);

      IR_send(decode_type,IR_data);
      
       irrecv.resume();
    }
    
  }
  //delay(3000);

}
