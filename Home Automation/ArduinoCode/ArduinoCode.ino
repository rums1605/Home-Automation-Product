#include<SoftwareSerial.h>
#include<Servo.h>

int enablePin = 5;

Servo servo;

char command;
String string;
#define led 12

  void setup()
  {
    digitalWrite(enablePin, HIGH);
    Serial.begin(9600);
    pinMode(led, OUTPUT);
    servo.attach(led);
    servo.write(90);
  }

  void loop()
  {
    digitalWrite(13, LOW);
    
    if (Serial.available() > 0) 
    {string = "";}
    
    while(Serial.available() > 0)
    {
      command = ((byte)Serial.read());
      
      if(command == ':')
      {
        break;
      }
      
      else
      {
        string += command;
      }
      
      delay(1);
    }
    
    if(string == "TO")
    {
        servo.write(0);
    }

    if(string == "TR")
    {
        servo.write(120);
    }
 }
 
