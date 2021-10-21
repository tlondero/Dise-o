/*******************************************************************************
 * INCLUDE HEADER FILES
 ******************************************************************************/
#include <Wire.h>      // libreria para bus I2C
#include <Adafruit_GFX.h>   // libreria para pantallas graficas
#include <Adafruit_SSD1306.h>   // libreria para controlador SSD1306
/*******************************************************************************
 * CONSTANT AND MACRO DEFINITIONS USING #DEFINE
 ******************************************************************************/
 
#define WIDTH 128     // reemplaza ocurrencia de ANCHO por 128
#define HEIGHT 64       // reemplaza ocurrencia de ALTO por 64
#define OLED_RESET 4      // necesario por la libreria pero no usado

/*******************************************************************************
 * VARIABLES  WITH FILE LEVEL SCOPE
 ******************************************************************************/
  
int TRIG = 10;      // trigger en pin 10
int ECO = 9;      // echo en pin 9
int LED = 3;      // LED en pin 3
int DURATION;
float DISTANCE;
float  lastvalDist;
float dist_out;
Adafruit_SSD1306 oled(WIDTH, HEIGHT, &Wire, OLED_RESET);  // crea objeto


/*******************************************************************************
 *******************************************************************************
 GLOBAL FUNCTION DEFINITIONS
 *******************************************************************************
 ******************************************************************************/
void setup()
{
  pinMode(TRIG, OUTPUT);  // trigger como salida
  pinMode(ECO, INPUT);    // echo como entrada
  Wire.begin();         // inicializa bus I2C
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C); // inicializa pantalla con direccion 0x3C

}

void loop()
{
  digitalWrite(TRIG, HIGH);     // generacion del pulso a enviar
  delay(1);       // al pin conectado al trigger
  digitalWrite(TRIG, LOW);    // del sensor
  
  DURATION = pulseIn(ECO, HIGH);  // con funcion pulseIn se espera un pulso
            // alto en Echo
  DISTANCE = DURATION / 58.2;    // distancia medida en centimetros
  dist_out=  (DISTANCE+lastvalDist)/2;
  lastvalDist=DISTANCE;
 // Serial.println(DISTANCE);    // envio de valor de distancia por monitor serial

  oled.clearDisplay();      // limpia pantalla

  oled.setTextColor(WHITE);   // establece color al unico disponible (pantalla monocromo)
  oled.setCursor(0,0);
  oled.setTextSize(1);      // establece tamano de texto en 1
  oled.print("SIMFS - - - By MAGT");  // escribe en pantalla el texto
  oled.setCursor(5, 15);     // ubica cursor en inicio de coordenadas 0,0
  oled.setTextSize(2);      // establece tamano de texto en 1
  oled.print("Distancia");  // escribe en pantalla el texto
  oled.setCursor(25, 45);     // ubica cursor en inicio de coordenadas 0,0
  oled.print((int)dist_out);  // escribe en pantalla el texto
  oled.print(" cm");
  oled.display();     // 
  delay(200);
}
