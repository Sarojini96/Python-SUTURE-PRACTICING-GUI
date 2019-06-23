

#include <SoftwareSerial.h>
SoftwareSerial blu(4,5);

float flexiForce;
float flexiForce1;
float x;
float y;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
blu.begin(9600);
analogRead(EXTERNAL);
}

void loop() {
  float Voltage=analogRead(A2);
  float Voltage1=analogRead(A0);
 
if (Voltage> 0)
 { Voltage/=1000;
  x=(28.053*(Voltage));
  flexiForce=x+0.2967;
  //Serial.print("force 1=");
  blu.print(flexiForce);
  blu.print("  ");
  delay(100);}
if (Voltage1>0) 
  Voltage1/=1000;
  y=(32.001*(Voltage1));
  flexiForce1=y+0.2707;
  //Serial.print("force 2=");
  blu.println(flexiForce1);   
  delay(100);
    }  
    
   
 

   
