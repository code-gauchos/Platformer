const int BUTTON_1 = 2, BUTTON_2 = BUTTON_1+1, BUTTON_3 = BUTTON_2+1;
const int LED = 5;

void setup() {
  Serial.begin(9600);
  
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);
  pinMode(BUTTON_3, INPUT);
  
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
}

void loop() {
  if(digitalRead(BUTTON_1) == LOW) {
    Serial.println("0");
  }
  else if(digitalRead(BUTTON_2) == LOW) {
    Serial.println("1");
  }
  else if(digitalRead(BUTTON_3) == LOW) {
    Serial.println("2");
  }
}
