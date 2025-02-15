import requests

# URL for the API
DRIVERSTANDINGS_URL = "https://api.jolpi.ca/ergast/f1/2024/driverstandings?"

# Fetch the response
requests.packages.urllib3.disable_warnings()
response = requests.get(DRIVERSTANDINGS_URL, verify=False).json()

try:
    # Navigate to the DriverStandings list
    standings = response['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    # Extract the top 10 positions, abbreviated driver names, and points
    top_10 = []
    for driver in standings[:10]:  # Get the first 10 entries
        position = driver['position']
        # Create abbreviated driver name (e.g., "L.Hamilton")
        driver_name = f"{driver['Driver']['givenName'][0]}.{driver['Driver']['familyName']}"
        points = driver['points']
        top_10.append((position, driver_name, points))

    # Print the top 10
    print("Top 10 Driver Standings:")
    for position, name, points in top_10:
        print(f"P{position}: {name} - {points} points")

except (KeyError, IndexError):
    print("Unable to retrieve driver standings. Check the API response format.")

