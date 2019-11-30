
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);

}

void loop() {
 char temp[100];
  if(Serial.available()){
    byte leng = Serial.readBytesUntil('g', temp, 20);
    
    Serial.print("Input data Lenght : ");
    Serial.println(leng);
    
    for(int i = 0; i < leng; i++){
      Serial.print(temp[i]);
    }
    Serial.println();
  }    
}
