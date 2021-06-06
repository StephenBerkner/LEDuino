#include <ESP8266WiFi.h>
#include <SPI.h>
#include <MD_Parola.h>                    // https://github.com/MajicDesigns/MD_Parola
#include <MD_MAX72xx.h>                   // https://github.com/MajicDesigns/MD_MAX72xx

#include "util.hpp"
#include "credentials.hpp"                // #define MY_SSID and MY_PASSWORD here

// Create MD_Parola display object to control MAX7219 LED Matrix and WiFi Server object
MD_Parola display = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);
WiFiServer server(SERVER_PORT);

void setup() {

  display.begin();                         // Initialize display
  display.setIntensity(0);                 // Set display brightness
  display.setSpeed(150);                   // Set display speed
  display.displayClear();                  // Clear display

  Serial.begin(115200);                    // Start Serial communication at 115200 Baud

  // Connect to the network with the credentials from server/credentials.hpp
  Serial.print("Trying to connect to ");
  Serial.println(MY_SSID);
  WiFi.begin(MY_SSID, MY_PASSWORD);

  // Loop until connected to network
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.print("\nLEDuino connected via IP: ");
  Serial.println(WiFi.localIP());          // Send the LEDuino IP address over Serial

  server.begin();                          // Begin listening on SERVER_PORT

}

/*
 * NOTE: The ESP8266 has a watchdog timer that must be restarted AT LEAST ONCE A SECOND
 */
void loop() {

  WiFiClient client = server.available();

  if (!client){
    return;
  }
    Serial.println("Client Connected");
    while (!client.available()){
      delay(1);
    }
    
    // Display string sent from client
    String toDisplay = client.readStringUntil('\n');

    //For debugging
    Serial.print("Received: ");
    Serial.println(toDisplay);
    
    //Display text scrolling to left
    display.displayText(toDisplay.c_str(), PA_LEFT,  100, 100, PA_SCROLL_LEFT, PA_SCROLL_LEFT);
    while (!display.displayAnimate()){
      // Necessary to avoid a soft WDT reset
      delay(1);
    }
    
    display.displayReset();
    client.flush();

  
}
