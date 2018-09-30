// For Arduino Uno
//int cameraPin = PD4;
//int ledPin = PD2;
//int potentiometerPin = A1;
//int sensorPin = A0;

//// For Adafruit Trinket M0
//int cameraPin = A3;
//int ledPin = A4;
//int potentiometerPin = A2;
//int sensorPin = A0;

// For Adafruit Trinket M0
int cameraPin = A3;
int ledPin = A2;
int potentiometerPin = A4;
int sensorPin = A0;

int soundVolume = 0;
int triggerLevel = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Starting");
  pinMode(cameraPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  digitalWrite(cameraPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  soundVolume = analogRead(sensorPin);
  triggerLevel = analogRead(potentiometerPin);
  Serial.print(soundVolume);
  Serial.print("\t");
  Serial.println(triggerLevel);
  if (soundVolume > triggerLevel)
  {
    digitalWrite(cameraPin, HIGH);
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(cameraPin, LOW);
    digitalWrite(ledPin, LOW);
    delay(100);
  }
  //  delay(5);
}
