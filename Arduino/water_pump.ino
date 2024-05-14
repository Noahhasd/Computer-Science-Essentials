int motor_pin = 8;

void setup() {
  pinMode(motor_pin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  int pause = 5000; 
  digitalWrite(motor_pin, HIGH);
  Serial.println("Turning Motor On");
  delay(pause);
  digitalWrite(motor_pin, LOW);
  Serial.println("Turning Motor Off");
  delay(pause);

}
