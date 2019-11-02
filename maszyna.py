import random
from itertools import islice
import webbrowser


filename = "#2_Spotkanie_Gda.xls"

with open(filename, 'r', encoding="utf-8") as file:

	# Read column titles
	first_line = file.readline().strip()
	titles = first_line.split("\t")
	
	# Count lines containing users
	user_cnt = 0;
	for line in file:
		if not line.isspace():
			user_cnt += 1

	# Pick a winner
	winner_id = random.randint(1, user_cnt)
	
	# Reset file line index
	file.seek(0)
	
	# Find winner data
	for line in islice(file, winner_id, winner_id + 1):
		winner_data = line.strip().split("\t")
		
		# Print winner data
		for i in range(len(winner_data)):
			print(titles[i] + ": " + winner_data[i])
		
		# Open winner profile in a browser
		input("\nPress Enter to open winner profile page...")
		webbrowser.open(winner_data[-1])
