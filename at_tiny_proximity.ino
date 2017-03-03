// hc-sr04.ino - distance using ultrasonic ping sensor
// (c) BotBook.com - Karvinen, Karvinen, Valtokari
int trigPin = 3;
int echoPin = 4;
int outputPin = 2;
//float v = 331.5 + 0.6 * 20; // Speed of sound at room temp in m/s *** May need to integrate temp sensor to make value correct ***

void setup(){
  pinMode(trigPin, OUTPUT); // Setup trigger pin for output
  pinMode(echoPin, INPUT); // Setup echo pin for input
  pinMode(outputPin, OUTPUT); // Setup output pin for output
}

float distanceCm(){
  digitalWrite(trigPin, LOW); // Initializes trigger pin to low
  delayMicroseconds(3); // Waits 3us for sensor to stabilize
  digitalWrite(trigPin, HIGH); // Sets pin to high to send burst signal
  delayMicroseconds(5); // Waits 5us while sending ultrasonic burst *** May need to change to 10us?? ***
  digitalWrite(trigPin, LOW); // Sets pin back to low to end burst signal 
  float tUs = pulseIn(echoPin, HIGH); // Measures the amount of time that the signal is taking to return
  float t = tUs / 1000.0 / 1000.0 / 2.0; // Converts to seconds and divides distance by 2 to get time
  //float d = t*v; // Time * Speed of sound (s*(m/s)) = m
  //return d*100; // Returns distance in centimeters ?? *** Correct units needs to be fixed in notation ***
  return t*100  //This is the time it took to receive the signal, still needs to be multiplied by speed of sound at specific temp
}

void loop(){ // Infinite loop
  int d=distanceCm(); // Gets distance in cm from function
  if(d < 10){digitalWrite(outputPin, HIGH);} // Logic to turn output pin HIGH if distance is less than a certain amount
  else{digitalWrite(outputPin, LOW);} // Logic to turn output pin LOW if distance is greater than a a certain amount
  delay(50); // Delay to restart new cycle ?? *** Fix notes to accurate description ***
}


