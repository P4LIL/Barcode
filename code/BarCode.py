import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time
import sys
from termios import tcflush, TCIOFLUSH


lcd=CharLCD(pin_rs=15, pin_rw=None, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD,
              cols=8, rows=2, dotsize=8)
              
backLight = 7
GPIO.setup(backLight,GPIO.OUT)      # lcd backlight

def LCDDisplay(text): 
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string(text[:8])    # write first 8 characters
    lcd.cursor_pos = (1, 0)
    lcd.write_string(text[8:16])    # write  8 - 16 characters 
    
while True:

    sys.stdout.flush()
    tcflush(sys.stdin, TCIOFLUSH)   # clear buffer
    
    LCDDisplay("Scan Barcode")

    barcode = raw_input()

    if barcode == 'A':
        LCDDisplay("  Healthy/Iach")
        GPIO.output(backLight,True)   
    elif barcode == 'B':        
        LCDDisplay(" Changed/Newid")
        GPIO.output(backLight,True)
    else:        
        LCDDisplay("? ? ? ? ? ? ? ? ")
        GPIO.output(backLight,True)   
    time.sleep(2)
    GPIO.output(backLight,False)
