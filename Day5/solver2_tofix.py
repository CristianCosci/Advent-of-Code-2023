with open('input.txt') as f:
    lines = f.readlines()
    seeds_fake = []
    maps = {}
    current_map = None
    for line in lines:
        if len(seeds_fake) == 0:
            seeds_fake = [int(x) for x in (lines[0].split(': ')[1].split())]
            seeds = []
            for i in range(0, len(seeds_fake), 2):
                for j in range(seeds_fake[i], seeds_fake[i]+seeds_fake[i+1]):
                    seeds.append(j)
            
            print(len(seeds))
            continue


        line = line.strip()

        if line.startswith("seed-to-soil map"):
            current_map = "seed-to-soil"
            maps[current_map] = []
        elif line.startswith("soil-to-fertilizer map"):
            current_map = "soil-to-fertilizer"
            maps[current_map] = []
        elif line.startswith("fertilizer-to-water map"):
            current_map = "fertilizer-to-water"
            maps[current_map] = []
        elif line.startswith("water-to-light map"):
            current_map = "water-to-light"
            maps[current_map] = []
        elif line.startswith("light-to-temperature map"):
            current_map = "light-to-temperature"
            maps[current_map] = []
        elif line.startswith("temperature-to-humidity map"):
            current_map = "temperature-to-humidity"
            maps[current_map] = []
        elif line.startswith("humidity-to-location map"):
            current_map = "humidity-to-location"
            maps[current_map] = []
        else:
            values = list(map(int, line.split()))
            if not len(values) == 0:
                maps[current_map].append(values)

    # print(seeds)
    # print(maps)
    location_list = []
    for seed in seeds:
        current_value = seed
        for current_map in list(maps.keys()):
            # print(current_map)
            for map_range in maps[current_map]:
                if current_value in range(map_range[1], map_range[1]+map_range[2]):
                    current_value = (current_value - map_range[1]) + map_range[0]
                    break
                    

        # print(current_value)
        location_list.append(current_value)
    
    print(min(location_list))