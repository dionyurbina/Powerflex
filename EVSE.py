import json
import csv

# JSON data
json_data = [
    {
        "Parking Space": "A1",
        "Serial Number": "SN123456",
        "Energy Delivered": "15.5 kWh"
    },
    {
        "Parking Space": "B2",
        "Serial Number": "SN234567",
        "Energy Delivered": "20.3 kWh"
    },
    {
        "Parking Space": "C3",
        "Serial Number": "SN345678",
        "Energy Delivered": "18.7 kWh"
    },
    {
        "Parking Space": "D4",
        "Serial Number": "SN456789",
        "Energy Delivered": "22.1 kWh"
    },
    {
        "Parking Space": "E5",
        "Serial Number": "SN567890",
        "Energy Delivered": "19.4 kWh"
    }
]

# Define the CSV file name
csv_file = 'cars.csv'

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Parking Space", "Serial Number", "Energy Delivered"])
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    writer.writerows(json_data)

print(f"JSON data has been successfully converted to {csv_file}.")

# Extract the Energy Delivered values and convert them to float
energy_delivered = [float(car["Energy Delivered"].split()[0]) for car in json_data]

# Calculate the average energy delivered
average_energy_delivered = sum(energy_delivered) / len(energy_delivered)

# Print the result
print(f"The average Energy Delivered is {average_energy_delivered} kWh.")