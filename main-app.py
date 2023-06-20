import requests
from bs4 import BeautifulSoup
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/weather/{id}")
def get_weather(id: int):
    # Send a GET request to the URL with the provided ID
    url = f"https://city.imd.gov.in/citywx/city_weather_test.php?id={id}"
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the past 24 hours weather data
    table = soup.find('table', attrs={'cellpadding': '0', 'cellspacing': '0', 'width': '100%'})

    # Find all the rows within the table
    rows = table.find_all('tr')
    details = {}

    # Iterate over the rows and extract the data
    for row in rows:
        data = row.find_all('td')
        if len(data) == 2:  # Check if the row contains two columns of data
            label = data[0].text.strip()
            value = data[1].text.strip()
            keyword = label.split('(')[0].strip()
            details[keyword] = value

    return details  # Return the details dictionary as JSON response

@app.get("/{path}")
def handle_404(path: str):
    return {"message": "Not found"}
