import time
import random
import os
import datetime

TEMP_FILE = "temperature.txt"

def read_temp_sensor():
    # Mocking sensor data for generic environment
    # In a real Raspberry Pi scenario, this might read from /sys/class/thermal/thermal_zone0/temp
    # or a GPIO connected sensor library.
    return round(random.uniform(20.0, 30.0), 2)

def main():
    print(f"Starting sensor reader. Writing to {os.path.abspath(TEMP_FILE)}")
    while True:
        try:
            temp = read_temp_sensor()
            with open(TEMP_FILE, "w") as f:
                f.write(str(temp))
            
            timestamp = datetime.datetime.now().isoformat()
            print(f"[{timestamp}] Read execution: {temp}°C")
            
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
