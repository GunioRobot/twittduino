
int outputPin = 13;
int col = 0;
int val =0;
void setup()
{
  Serial.begin(115200);
  pinMode(outputPin, OUTPUT);
  Serial.print(186,BYTE);
  delay(200);
  Serial.print(127,BYTE);
  delay(200);

}

void loop()
{
  if (Serial.available()) {
    val = Serial.read();

    if(val == '~'){
      limpia(0);
      val = 0;
    }

   if(val == '`'){
          col++;
          salta(col);
          val =0;
        }

   if(val == '¤'){ //opt6
          blink();
          val =0;
   }
          manda(val);
  }
}

void manda(int vale){
if(vale < 32 || vale > 123){
  vale = 32;
}
              Serial.print(vale,BYTE);
              delay(20);
              Serial.print(255,BYTE);
              delay(20);
              Serial.print(190,BYTE);
              delay(20);
}

void limpia(int offset){
      Serial.print(186,BYTE);
      delay(100);
      Serial.print(127 + offset,BYTE);
      delay(100);
}

void salta(int offset){
      Serial.print(127 + offset,BYTE);
      delay(200);
}

void blink(){
      Serial.print(185,BYTE);
      delay(200);
      delay(500);
      Serial.print(185,BYTE);
      delay(200);
}
