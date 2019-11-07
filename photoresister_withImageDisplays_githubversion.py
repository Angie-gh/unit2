from microbit import *
#>>>>>This script is used with a breadboard and photoresister 
#>>>>>The LED display on the micro:bit controller toggles between showing a sinking boat and a happy face<<<<<
 
#>>>>>The photoresister is wired to receive signal on pin0<<<<<
calibrationVal = pin0.read_analog()
sleep(1000)
#>>>>>Images from micro:bit that depict a boat sinking<<<<<
boat1 = Image("05050:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

boat2 = Image("00000:"
              "05050:"
              "05050:"
              "05050:"
              "99999")

boat3 = Image("00000:"
              "00000:"
              "05050:"
              "05050:"
              "05050")

boat4 = Image("00000:"
              "00000:"
              "00000:"
              "05050:"
              "05050")

boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "05050")

boat6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

#>>>>>Initialize variables<<<<<
all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
#>>>>>Below variable to prevent the 'sinking boat' from sinking more than once <<<<<
boatflag=0

#>>>>>Creating a continuous loop for the photoresister to decide when to display sinking ships or a happy face
#>>>>>To test:  User places hand over the photoresister <<<<<
while True:
    lightVal = pin0.read_analog()
    #>>>>>Checking whether the light sensor is blocked. <<<<<
    if lightVal < calibrationVal-50:
        #>>>>>If the sensor is blocked, displaying an LED light as well as a happy face <<<<<
        pin16.write_digital(1)
        display.show(Image.HAPPY)
        boatflag=0
    else:
        #>>>>>If the sensor is blocked, turing off the LED and displaying a sinking boat <<<<<
        if boatflag==0:
            pin16.write_digital(0)
            display.show(all_boats, delay=200)
            boatflag=1
    