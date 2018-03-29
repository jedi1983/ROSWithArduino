#include <AccelStepper.h>


// Define a stepper motor 1 for arduino 
// direction Digital 9 (CW), pulses Digital 8 (CLK)
AccelStepper stepper(1, 9, 8);
void setup()
{  
  // Change these to suit your stepper if you want
  stepper.setMaxSpeed(4000);//1100
  stepper.setAcceleration(6000);
  stepper.moveTo(4000);
}

void loop()
{
    // If at the end of travel go to the other end
    if (stepper.distanceToGo() == 0){
      stepper.moveTo( -stepper.currentPosition() );
    }
    
    stepper.run();
}
