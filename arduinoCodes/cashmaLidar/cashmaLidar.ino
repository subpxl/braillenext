//-------------imports-----------
#include <Wire.h>
#include <VL53L1X.h>

//-----------defines---------
#define coin  6  // find its pin on pro mini
#define numReadings 10

//---------instances and declearations-----------
VL53L1X lidar;  /// global

//--------variable declearations----------
int readings[numReadings];      // the readings from the analog input
int readIndex = 0;              // the index of the current reading
int total = 0;                  // the running total
int average = 0;  
int newav;
int i = 0;
int fadeValue;
int cm;


//---------void setup-----------
void setup()
{
  pinMode(coin, OUTPUT);
  Serial.begin(115200);
  
  Wire.begin();
  Wire.setClock(400000); // use 400 kHz I2C

  lidar.setTimeout(500);
  if (!lidar.init())
  {
    Serial.println("Failed to detect and initialize lidar!");
    while (1);
  }
    lidar.setDistanceMode(VL53L1X::Long);
  lidar.setMeasurementTimingBudget(50000);
  lidar.startContinuous(50);
}

//-------int average function------------
int av(int b)
{
  total = total - readings[readIndex];
  // read from the lidar:
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

  average = total / numReadings; // calculate the average:
   return b;   //this is optional , needs to be tested
  //return average;
}

//-------void buzz function----------
void buzz(int k)
{
  k = k/15;
  digitalWrite(coin,HIGH);
 delay(k);
 digitalWrite(coin,LOW);
 delay(k);
}

//-----------void loop----------
void loop() {
  digitalWrite(coin,LOW);

  long duration, distance;

  distance = lidar.read();

  newav = av(distance);

  if (newav >= 3500 || newav <= 0){
    Serial.println("Out of range");
  }
  
  else 
  {
      cm = 3510 - newav;  
  //fadeValue = map(cm , 0, 250, 0, 254);
fadeValue = map(cm , 0, 250, 0, 254);

  analogWrite(coin, fadeValue);  // Writes the fadeValue to pin 9 
    buzz(fadeValue);    //this is for vibrating on and off 
  Serial.println(newav);
  }
}  