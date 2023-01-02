damages = "$7M;$15B;$151M;Damages Not Recorded;452B" #initial list of uncleaned data
damages_split = damages.split(";")
damages_updated = []
for item in damages_split: #for loop that cleans the data into 'damages_updated'
	item = item.replace("$","")
	if "M" in item:
		item = item.replace("M","")
		item = int(item)*1000000
		damages_updated.append(item)

	elif "B" in item:
		item = item.replace("B","")
		item = int(item)*1000000000
		damages_updated.append(item)

	else:
		damages_updated.append(item)

damages_sum = 0 #Variables used to find the average hurricane damage dollar cost
count = 0
for item in damages_updated:
	if type(item) == type(damages_updated[0]):
		damages_sum += item
		count += 1

average_damage = damages_sum / count #We print the average damage
print("Given the initial list of damages: " + damages)
print("The average hurricane damage has a monetary cost of: ${:,}".format(average_damage))