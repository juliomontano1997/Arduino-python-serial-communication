char dato = '0';  
void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  Serial.write("Estoy listo\n");
}

void loop()
{  
    if(Serial.available())
    {
      dato = Serial.read();
      if (dato=='1')
      {
        digitalWrite(13, HIGH);   
        delay(3000);
      }
      else if(dato=='0')
      {
         digitalWrite(13, LOW);
      }
    }   
}
