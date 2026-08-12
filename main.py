from machine import Pin, I2C, RTC
from ssd1306 import SSD1306_I2C
import time

# Initialize I2C and OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust pins as per your board
oled = SSD1306_I2C(128, 64, i2c)

# Initialize RTC
rtc = RTC()

# Set initial time (if needed)
# Format: (year, month, day, weekday, hours, minutes, seconds, subseconds)
# Example: Set to 2025-05-27 15:45:00
rtc.datetime((2025, 5, 27, 2, 15, 45, 0, 0))  # Adjust as per current time

def display_time():
    while True:
        # Get current time from RTC
        current_time = rtc.datetime()
        hours = current_time[4]
        minutes = current_time[5]
        seconds = current_time[6]
        
        # Format time as HH:MM:SS
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        
        # Clear display
        oled.fill(0)
        
        # Display time centered
        oled.text("Digital Clock", 20, 10)
        oled.text(time_str, 35, 30)
        
        # Optional: Display date
        date_str = "{:02d}-{:02d}-{:04d}".format(current_time[2], current_time[1], current_time[0])
        oled.text(date_str, 30, 50)
        
        # Update display
        oled.show()
        
        # Update every second
        time.sleep(1)

# Run the clock
try:
    display_time()
except KeyboardInterrupt:
    oled.fill(0)
    oled.text("Clock Stopped", 20, 30)
    oled.show()