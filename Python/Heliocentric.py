earth_days = input("Enter input for Earth: ")
mars_days = input("Enter input for Mars: ")
counter = 0
while (True):
	if mars_days % 687 == 0 and earth_days % 365 == 0:
		break
	counter += 1; earth_days += 1; mars_days += 1;

print counter