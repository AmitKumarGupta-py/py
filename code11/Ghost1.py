import time

for i in range(100):
	print(f"\rProgress:{i+1}%",end='')
	time.sleep(0.1)
	
print("\nDone!")

