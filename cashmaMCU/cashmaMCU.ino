#define trigPin1 17
#define echoPin1 18
#define coin2 19

int i = 0;

int fadeValue1 ;
int cm1;



const int numReadings = 10;

int readings[numReadings];      // the readings from the analog input
int readIndex = 0;              // the index of the current reading
int total = 0;                  // the running total
int average = 0;  

int newav  ;



void setup() {
  Serial.begin (9600);
  
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(coin2, OUTPUT);

      for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
}
}




int av(int b)
{

  
 total = total - readings[readIndex];
  // read from the sensor:
  readings[readIndex] = b;
  // add the reading to the total:
  total = total + readings[readIndex];
  // advance to the next position in the array:
  readIndex = readIndex + 1;

  // if we're at the end of the array...
  if (readIndex >= numReadings) {
    // ...wrap around to the beginning:
    readIndex = 0;
  }

  // calculate the average:
  average = total / numReadings;
  // send it to the computer as ASCII digits
 

return b;
  }


  
void loop() {

long duration1, distance1;
digitalWrite(trigPin1, LOW);  // Added this line
delayMicroseconds(2); // Added this line
digitalWrite(trigPin1, HIGH);
//  delayMicroseconds(1000); - Removed this line
delayMicroseconds(10); // Added this line
digitalWrite(trigPin1, LOW);
duration1 = pulseIn(echoPin1, HIGH);
distance1 = (duration1/2) / 29.1;
delay(10);
newav = av(distance1);
   
if (newav >= 250 || newav <= 0){
    Serial.println("Out of range");
  }
else {
    cm1 = 250 - newav;  
    fadeValue1 = map(cm1 , 0, 250, 0, 254);
    analogWrite(coin2, fadeValue1);  // Writes the fadeValue to pin 9 
    Serial.println(newav);
    Serial.print("\t");
    //   Serial.println(fadeValue1);
    Serial.println(cm1);
  }
  //delay(4);
 //i++;
}
