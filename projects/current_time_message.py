from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S %p")

print("The time is", current_time)