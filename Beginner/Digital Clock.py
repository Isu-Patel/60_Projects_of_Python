import time
import os
import msvcrt

print("Digital Clock - Press 'q' to quit")
while True:
    os.system('cls')
    current_time = time.strftime("%H:%M:%S")
    print(f"Digital Clock: {current_time}")
    print("Press 'q' to quit")
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()
        if key == 'q':
            break
    
    time.sleep(1)