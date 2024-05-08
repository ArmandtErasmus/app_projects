import iss
import time
import os

url = 'https://api.wheretheiss.at/v1/satellites/25544'

def Coordinates(lat, long):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The lat/long of the ISS is currently: {lat}, {long} \nPress CTRL+C to quit.")

if __name__=="__main__":
    
    try:
        iss_object = iss.GetData(url)

        while True:

            time.sleep(2)
            iss_location_data = iss_object.get_response()
            iss_longitude, iss_latitude = iss_location_data['longitude'], iss_location_data['latitude']
            Coordinates(iss_latitude, iss_longitude)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Program terminated by user.")
        

