print("Calculate fuel consumption.")
Feed = input("Enter travel distance (kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel used (liters): ")
FuelUsage = int(Feed)
Consumption = (FuelUsage / Distance) * 100
Consumption = int(Consumption)
print(f"Fuel consumption is {Consumption} l per 100 km")