from sense_hat import SenseHat
from time import sleep
from datetime import datetime
from csv import writer
import csv

sense = SenseHat()

# Innstillingar
tidsstempel = datetime.now()
forsinkelse = 1
listeVerdata = []

# Maaling, basert paa https://projects.raspberrypi.org/en/projects/sense-hat-data-logger
with open('verdata.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    while True:
        pressure = sense.get_pressure()
        print("Trykk:",round(pressure,2))
        listeVerdata.append(pressure)
        
        temp = sense.get_temperature()
        print("Temperatur:",round(temp,2))
        listeVerdata.append(temp)
        
        humidity = sense.get_humidity()
        print("Fuktighet:",round(humidity,2))
        listeVerdata.append(humidity)
        
        dt = listeVerdata[-1] - tidsstempel
        if dt.seconds > forsinkelse:      
            writer.writerow(listeVerdata)
            print("Full liste denne runden:",listVerdata)