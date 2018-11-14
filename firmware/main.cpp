#include "Particle.h"

SYSTEM_MODE(MANUAL);
SYSTEM_THREAD(ENABLED);

void setup() // Put setup code here to run once
{
        Serial.begin(115200);
}

long counter = 0;

void loop() // Put code here to loop forever
{
        Serial.printlnf("%ld, %ld", counter, millis());

        counter++;
        delay(10);
}
