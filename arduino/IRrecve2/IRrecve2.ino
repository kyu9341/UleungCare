
#include <IRremote.h>
 
int recvPin = 2;
IRrecv irrecv(recvPin);

void  setup ( )
{
  Serial.begin(9600);   // Status message will be sent to PC at 9600 baud
  irrecv.enableIRIn();  // Start the receiver
}
 

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
 
//+=============================================================================
// The repeating section of the code
//
void  loop ( )
{
  decode_results  results;        // Somewhere to store the results
 
  if (irrecv.decode(&results)) {  // Grab an IR code
    dumpCode(&results);           // Output the results as source code
    irrecv.resume();              // Prepare for the next value
  }
}
