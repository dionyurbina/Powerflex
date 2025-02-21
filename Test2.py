import requests
import json
import csv
import os

# Define the CSV file name
csv_file = 'cars.csv'
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

def get_data(evsedata):
    print(evsedata)
    return evsedata
#['Parking Space']['Serial Number']['Energy Delivered']

def parse_json():
    baseurl = "https://rickandmortyapi.com/api/character"
    data = main_request(baseurl)
    '''
    for evse_data in data:
        parking_space = evse_data["Parking Space"]
        serial_number = evse_data["Serial Number"]
        energy_delivered = evse_data["Energy Delivered"]
    '''
    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Parking Space", "Serial Number", "Energy Delivered"])
        # Write the header
        writer.writeheader() 
        # Write the data
        writer.writerows(data)
    file.close()

    total_delivered = 0
    for evse_data in data:
        energy_delivered = float(evse_data["Energy Delivered"].split()[0])
        total_delivered = total_delivered + energy_delivered
    
    avg_delivered = total_delivered / len(data)
    print(avg_delivered)

def main_request(baseurl_copy):
    r = requests.get(baseurl_copy)
    data = r.json() 
    return json_data

parse_json()