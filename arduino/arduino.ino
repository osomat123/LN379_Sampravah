const int trigPin = 7;
const int echoPin = 6;
long duration;
int distanceCm, distanceInch;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(20);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * 0.0340 / 2;
  //distanceInch = duration * 0.01330 / 2;
  Serial.println(distanceCm);
  delay(10000);
}
