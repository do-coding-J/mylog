void setup() {
  // 시리얼 통신을 시작하고, 데이터 전송 속도를 115200으로 설정합니다.
  Serial.begin(115200);
}

void loop() {
  // "Hello, World!"를 시리얼 포트를 통해 전송합니다.
  Serial.println("Hello, World!");
  delay(1000); // 1초 지연
}
