
#define coin1 6
#define coing1 10

#define trigPin 17
#define echoPin 18

#define buzzpos 19
#define buzzneg 7

#define numReadings 10

int readings[numReadings];      // the readings from the analog input
int readIndex = 0;              // the index of the current reading
int total = 0;                  // the running total
int average = 0;  

int newav;

int i = 0;

int fadeValue;
int cm;


void setup() {
  Serial.begin (9600);
  pinMode(buzzpos, OUTPUT);
  pinMode(buzzneg, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(coin1, OUTPUT);
    pinMode(coing1, OUTPUT);
     
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



void buzz(int k)
{digitalWrite(buzzpos,HIGH);
 delay(k);
 digitalWrite(buzzpos,LOW);
 delay(k);
}

void loop() {
  digitalWrite(coing1,LOW);
  digitalWrite(buzzneg,LOW);

  long duration, distance;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
//  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
 delay(5);


newav = av(distance);

  if (newav >= 250 || newav <= 0){
    Serial.println("Out of range");
  }
  
  else 
  {


      cm = 250 - newav;  

  fadeValue = map(cm , 0, 250, 0, 254);


  analogWrite(coin1, fadeValue);  // Writes the fadeValue to pin 9 
    buzz(fadeValue);
    Serial.println(newav);
   // Serial.print("\t");
     //   Serial.println(fadeValue1);
      //Serial.println(i);

  }

 i++;
}
