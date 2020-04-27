import json

# Explore the structure of the data

filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
	#json.load converts the data into a giant dictionary
	all_eq_data = json.load(f)

# create a more readable file
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	# json.dump takes a json data object and file and writes the data to the file
	json.dump(all_eq_data, f, indent=4)