import re

# Apri il file e leggi le linee
with open("input.txt", "r") as file:
    lines = file.readlines()

# Inizializza le variabili
time_value = ""
distance_value = ""

# Loop attraverso le linee e estrai i numeri
for line in lines:
    # Usa una espressione regolare per trovare tutti i numeri nella linea
    numbers = re.findall(r'\d+', line)
    
    # Concatena i numeri e assegna alle variabili appropriate
    if line.startswith("Time:"):
        time_value = ''.join(numbers)
    elif line.startswith("Distance:"):
        distance_value = ''.join(numbers)

time_value = int(time_value)
distance_value = int(distance_value)

result = 1

t = time_value
record = distance_value
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