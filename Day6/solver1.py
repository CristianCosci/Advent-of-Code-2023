import re

with open("input.txt", "r") as file:
    lines = file.readlines()

    time_values = []
    distance_values = []

    for line in lines:
        # Usa una espressione regolare per trovare tutti i numeri nella linea
        numbers = re.findall(r'\d+', line)

        if line.startswith("Time:"):
            time_values.extend(map(int, numbers))
        elif line.startswith("Distance:"):
            distance_values.extend(map(int, numbers))


    result = 1
    for i in range(len(time_values)):
        t = time_values[i]
        record = distance_values[i]
        count = 0
        v = 0

        for _ in range(t):
            distance = v * t
            if distance > record:
                count += 1
            
            t -= 1
            v += 1
        
        result *= count
    
    print(result)
