def create_mapping(all_input, start, stop, sources):
    mapping = {source:source for source in sources}
    for line in range(start, stop+1):
        vals = all_input[line].strip().split(" ")
        destination_range_start = eval(vals[0])
        source_range_start = eval(vals[1])
        range_length = eval(vals[2])

        if len(range(max(min(sources), source_range_start), min(max(sources), source_range_start + range_length))):
            for source in mapping.keys():
                if source in range(source_range_start, source_range_start + range_length):
                    offset = source - source_range_start
                    mapping[source] = destination_range_start + offset
    return mapping

all_input = []
with open("input_5.txt") as f:
    for line in f:
        all_input.append(line.strip())

seeds = [eval(seed) for seed in all_input[0].split(":")[1].split(" ") if seed]
print("SEEDS", seeds)

seed_to_soil = create_mapping(all_input, 3,29, seeds)
print("SEED TO SOIL", seed_to_soil)

soil_to_fertilizer = create_mapping(all_input, 32,51, seed_to_soil.values())
print("SOIL TO FERTILIZER", soil_to_fertilizer)

fertilizer_to_water = create_mapping(all_input, 54,101, soil_to_fertilizer.values())
print("FERTILIZER TO WATER", fertilizer_to_water)

water_to_light = create_mapping(all_input, 104,145, fertilizer_to_water.values())
print("WATER TO LIGHT", water_to_light)

light_to_temperature = create_mapping(all_input, 148,171, water_to_light.values())
print("LIGHT TO TEMPERATURE", light_to_temperature)

temperature_to_humidity = create_mapping(all_input, 174,198, light_to_temperature.values())
print("TEMPERATURE TO HUMIDITY", temperature_to_humidity)

humidity_to_location = create_mapping(all_input, 201,237, temperature_to_humidity.values())
print("HUMIDITY TO LOCATION", humidity_to_location)

print(min(humidity_to_location.values()))