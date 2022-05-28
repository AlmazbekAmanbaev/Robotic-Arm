
#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time
 
servo1 = 17
servo2 = 18
servo3 = 19
servo4 = 20
servo5 = 21
servo6 = 22
  
pwm = pigpio.pi() 
pwm.set_mode(servo1, pigpio.OUTPUT)
pwm.set_mode(servo2, pigpio.OUTPUT)
pwm.set_mode(servo3, pigpio.OUTPUT)
pwm.set_mode(servo4, pigpio.OUTPUT)
pwm.set_mode(servo5, pigpio.OUTPUT)
pwm.set_mode(servo6, pigpio.OUTPUT)
 
pwm.set_PWM_frequency( servo1, 50 )
pwm.set_PWM_frequency( servo2, 70 )
pwm.set_PWM_frequency( servo3, 50 )
pwm.set_PWM_frequency( servo4, 50 )
pwm.set_PWM_frequency( servo5, 50 )
pwm.set_PWM_frequency( servo6, 50 )
 
 
def zeroDegrees():
    print( "0 deg" )
    print( "Setting all values to Zero" )

    pwm.set_servo_pulsewidth( servo1, 1125 ) ;
    time.sleep( 3 )
    pwm.set_servo_pulsewidth( servo2, 650 ) ;
    time.sleep( 3 )
    pwm.set_servo_pulsewidth( servo3, 550 );
    time.sleep( 3 )
    pwm.set_servo_pulsewidth( servo4, 1500 );
    time.sleep( 3 )
    pwm.set_servo_pulsewidth( servo5, 1500 );
    time.sleep( 3 )
    pwm.set_servo_pulsewidth( servo6, 1300 );
    time.sleep( 3 )
    
    print( "Finished setting all values to Zero" )
    
def PartOne():
    print("Step 1 Part 1")
    print( "Setting all values to Position One" )

    time.sleep( 1 )
    pwm.set_servo_pulsewidth( servo6, 1400 );
    time.sleep( 1 )
    pwm.set_servo_pulsewidth( servo5, 1470 );
    time.sleep( 1 )
    for x in range(650, 1200):
        pwm.set_servo_pulsewidth( servo2, x ) ;
        time.sleep(0.01)
    time.sleep( 1 )
    for x in range(1470, 1500):
        pwm.set_servo_pulsewidth( servo5, x );
        time.sleep(0.01)
    time.sleep( 1 )
    for x in range(550, 1500):
        pwm.set_servo_pulsewidth( servo3, x );
        time.sleep(0.01)
    time.sleep( 1 )
    pwm.set_servo_pulsewidth( servo5, 1500 );
    time.sleep( 1 )
    for x in range(1200, 1620):
        pwm.set_servo_pulsewidth( servo2, x );
        time.sleep(0.01)
    time.sleep( 1 )
    for x in range(1500, 2400):
        pwm.set_servo_pulsewidth( servo5, x );
        time.sleep(0.01)
    time.sleep( 1 )
    pwm.set_servo_pulsewidth( servo6, 500 );
    time.sleep( 1 )
    print( "Finished setting all values to Position One" )


def Return():
    print("Return")
    print( "Setting all values to Return" )

    time.sleep( 1 )
    for x, y in zip(range(1620, 650, -97), range(1500, 550, -95)):
        pwm.set_servo_pulsewidth( servo2, x ) ;
        time.sleep(0.5)
        pwm.set_servo_pulsewidth( servo3, y ) ;
        time.sleep(2)
        
    print( "Finished setting all values to Return" )

        
def Task2():
    print("Task 2")
    print( "Setting all values to Position Two" )

    time.sleep( 1 )
    pwm.set_servo_pulsewidth( servo1, 1500 ) ;
    time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 650);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 550 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 747);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 645 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 844);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 740 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 941);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 835 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1038);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 930 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1135);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 1025 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1232);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 1120 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1329);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 1215 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1426);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 1310 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1523);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 1405 ) ;
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo2, 1620);
    # time.sleep( 1 )
    # pwm.set_servo_pulsewidth( servo3, 1500 ) ;
    # time.sleep( 1 )
    for x, y in zip(range(650, 1620, 97), range(550, 1500, 95)):
        pwm.set_servo_pulsewidth( servo2, x ) ;
        time.sleep(1)
        pwm.set_servo_pulsewidth( servo3, y ) ;
        time.sleep(1)
    print( "Enabling Dinsinfector" )
    time.sleep(2)
    print( "Finsihed Dinsinfector" )
    time.sleep(1)
    print( "Finished setting all values to Task Two" )

        
def Task3():
    print("Task 3")
    print( "Setting all values to Position Three" )
    
    for x, y in zip(range(650, 1620, 97), range(550, 1500, 95)):
        pwm.set_servo_pulsewidth( servo2, x ) ;
        time.sleep(1)
        pwm.set_servo_pulsewidth( servo3, y ) ;
        time.sleep(1)
        
    print( "Finished setting all values to Task Three" )


# pwm.set_servo_pulsewidth( servo5, 2300 );
# time.sleep( 3 )
# pwm.set_servo_pulsewidth( servo6, 1300 );
# time.sleep( 3 )
# zeroDegrees()
zeroDegrees()
# #
# pwm.set_servo_pulsewidth( servo5, 500 );
# time.sleep( 3 )
# pwm.set_servo_pulsewidth( servo5, 1500 );
# time.sleep( 3 )
# pwm.set_servo_pulsewidth( servo5, 2500 );
# time.sleep( 3 )
# print( "90 deg" )
# pwm.set_servo_pulsewidth( servo3, 1500 ) ;
# time.sleep( 3 )
 
# print( "180 deg" )
# pwm.set_servo_pulsewidth( servo, 2500 ) ;
# time.sleep( 3 )
#  
# # turning off servo
pwm.set_PWM_dutycycle(servo1, 0)
pwm.set_PWM_dutycycle(servo2, 0)
pwm.set_PWM_dutycycle(servo3, 0)
pwm.set_PWM_dutycycle(servo4, 0)
pwm.set_PWM_dutycycle(servo5, 0)
pwm.set_PWM_dutycycle(servo6, 0)

pwm.set_PWM_frequency(servo1, 0)
pwm.set_PWM_frequency(servo2, 0) 
pwm.set_PWM_frequency(servo3, 0) 
pwm.set_PWM_frequency(servo4, 0) 
pwm.set_PWM_frequency(servo5, 0) 
pwm.set_PWM_frequency(servo6, 0) 
