import math
import datetime
import random

now=datetime.datetime.now()
print("\nCurrent date and time: ",now.strftime("%Y-%m-%d  %H:%M:%S"))

num=random.randint(1,100)
print("\nRandom number generated: ",num)
fruit=["apple","cherry","banana"]
print("Random fruit: ",random.choice(fruit))

print("\nSquare root of 16: ",math.sqrt(16))
print("pi= ",math.pi)
print("sine of 90 degree: ",math.sin(math.radians(90)))

eoy=datetime.datetime(now.year,12,31)
daysleft=(eoy-now).days
print(f"\nDays left in the year:{daysleft}")
