# A REST API to Get Weather Details from IMD

This API allows you to retrieve weather details from the India Meteorological Department (IMD) website by providing a city ID.

**Disclaimer:** All credit belongs to the India Meteorological Department. Please note that the API may not work if the website's code is changed, as it relies on web scraping.

## Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>
2. Navigate to the project directory:

    ```shell
    cd <project_directory>

3. Create and activate a virtual environment:
   ```shell
   python3 -m venv venv
   source venv/bin/activate
4. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    
## Usage
   
 1. Run the FastAPI server:
     ```shell
     uvicorn main-app:app --reload
 2. Open your web browser and visit the following URL:
      ```shell
      http://localhost:8000/weather/{id}
 3. Replace {id} in the URL with the desired city ID.

 4. The API will return the weather details for the specified city as a JSON response.

## API Documentation

`GET /weather/{id}`
Returns the weather details for the specified city.

Parameters:

`id` (integer): The city ID.
Example Request:
    
    `GET /weather/90060`
Example Response:
  ```shell
  {
    "Maximum Temp": "33.5",
    "Departure from Normal": "2",
    "Minimum Temp": "26.4",
    "24 Hours Rainfall": "NIL",
    "Relative Humidity at 0830 hrs": "82",
    "Relative Humidity at 1730 hrs": "82",
    "Todays Sunset": "18:52",
    "Tomorrow's Sunrise": "06:05",
    "Moonset": "20:53",
    "Moonrise": "07:42"
  }
