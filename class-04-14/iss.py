import requests
import datetime

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

r = response.json()

print(r)

timestamp = r['timestamp']
timestamp = datetime.datetime.fromtimestamp(timestamp) # convert from epoch time to readable date and time
timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
longitude = r['iss_position']['longitude']
latitude = r['iss_position']['latitude']

print(f"Timestamp: {timestamp}")
print(f"Longitude: {longitude}")
print(f"Latitude: {latitude}")

lines = [timestamp, "\n", longitude, "\n", latitude]
with open('/data/output.txt', 'w') as f:
    f.writelines(lines)