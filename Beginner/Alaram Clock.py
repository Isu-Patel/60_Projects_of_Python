import time
import winsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")
print(f"Alarm set for {alarm_time}")

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("ALARM! Time's up!")
        for _ in range(5):
            winsound.Beep(1000, 1000)  # 1000Hz for 1 second
        break
    time.sleep(1)  # Check every second