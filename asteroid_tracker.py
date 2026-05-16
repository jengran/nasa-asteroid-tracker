import requests
from datetime import date, timedelta

# Your NASA API key
API_KEY = "QdHq9uKcKwC45Nsv5tTZp4B4ChN5VHJYkHTO27Pf"

# Today's date and 7 days from now
today = date.today()
end_date = today + timedelta(days=7)

# Ask NASA for asteroid data
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={end_date}&api_key={API_KEY}"

response = requests.get(url, timeout=10)
data = response.json()

print("Connected to NASA!")
print(f"Total asteroids this week: {data['element_count']}")
print("-" * 40)

for date_key in data['near_earth_objects']:
    for asteroid in data['near_earth_objects'][date_key]:
        name = asteroid['name']
        hazardous = asteroid['is_potentially_hazardous_asteroid']
        diameter = asteroid['estimated_diameter']['meters']['estimated_diameter_max']
        speed = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
        distance = asteroid['close_approach_data'][0]['miss_distance']['kilometers']

        print(f"\n🌑 {name}")
        print(f"   Diameter: {diameter:.0f} meters")
        print(f"   Speed: {float(speed):,.0f} km/h")
        print(f"   Distance from Earth: {float(distance):,.0f} km")
        print(f"   Hazardous: {'⚠️ YES' if hazardous else '✅ No'}")