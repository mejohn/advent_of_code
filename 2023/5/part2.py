from itertools import pairwise
import ipdb

def create_mapping(all_input, start, stop, source_ranges):
    destination_ranges = set()
    for line in range(start, stop+1):
        vals = all_input[line].strip().split(" ")
        destination_range_start = eval(vals[0])
        source_range_start = eval(vals[1])
        range_length = eval(vals[2])
        
        for source_range in source_ranges:
            overlap = range(max(source_range[0], source_range_start), min(source_range[1], source_range_start + range_length))
            if len(overlap):
                min_offset = overlap[0] - source_range_start
                max_offset = source_range_start + range_length - overlap[-1]
                destination_ranges.add((destination_range_start + min_offset, destination_range_start + max_offset + range_length))
    return sorted(destination_ranges, key=lambda x: x[0])

all_input = []
with open("input_5.txt") as f:
    for line in f:
        all_input.append(line.strip())

print(all_input)
seeds = []
old_seeds = [eval(seed) for seed in all_input[0].split(":")[1].split(" ") if seed]
paired_seeds = pairwise(old_seeds)
for start,length in paired_seeds:
    seeds.append((start, start+length))
print("SEEDS", seeds)

seed_to_soil = create_mapping(all_input, 3,29, seeds)
print("SEED TO SOIL", seed_to_soil)

soil_to_fertilizer = create_mapping(all_input, 32,51, seed_to_soil)
print("SOIL TO FERTILIZER", soil_to_fertilizer)

fertilizer_to_water = create_mapping(all_input, 54,101, soil_to_fertilizer)
print("FERTILIZER TO WATER", fertilizer_to_water)

water_to_light = create_mapping(all_input, 104,145, fertilizer_to_water)
print("WATER TO LIGHT", water_to_light)

light_to_temperature = create_mapping(all_input, 148,171, water_to_light)
print("LIGHT TO TEMPERATURE", light_to_temperature)

temperature_to_humidity = create_mapping(all_input, 174,198, light_to_temperature)
print("TEMPERATURE TO HUMIDITY", temperature_to_humidity)

humidity_to_location = create_mapping(all_input, 201,237, temperature_to_humidity)
print("HUMIDITY TO LOCATION", humidity_to_location)

print(sorted(humidity_to_location, key=lambda x: x[0]))
ipdb.set_trace()

# print(sorted(locations, key=lambda x: x.destination_start, reverse=True))