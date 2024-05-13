int relayPin = 8; // Pin connected to relay module

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(relayPin, OUTPUT); // Set relay pin as output
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read command from serial
    
    if (command == '1') {
      digitalWrite(relayPin, HIGH); // Turn relay ON
      Serial.println("Relay is ON");
    } else if (command == '0') {
      digitalWrite(relayPin, LOW); // Turn relay OFF
      Serial.println("Relay is OFF");
    }
  }
  delay(10);
}
