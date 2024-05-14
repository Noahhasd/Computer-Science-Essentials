void setup() {
  pinMode(A0, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  float water_value = analogRead(A0);
  Serial.print("WaterLevel: ");
  Serial.println(water_value);
  delay(1000);
}
