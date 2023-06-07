# Weather App

This project is a weather application that utilizes the OpenWeather API to gather weather data. It is built using Django, a Python web framework, for data retrieval and processing, and HTML and CSS to create a webpage for displaying weather information based on user input (city name).

![Imgur](https://i.imgur.com/mdWfoEa.png)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Resources](#resources)

## Installation

1. **Clone** the repository:

    ```bash
    git clone https://github.com/your-username/weather-app.git
    ```
2. **Install** the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Sign up for an API key at OpenWeather and obtain your API key.

4. Create a file named config.py in the weather_app directory. Inside the file, add the following line and replace 'YOUR_API_KEY' with your actual API key:
    ```python
    YOUR_API_KEY
    ```


## Usage

1. Navigate to the project directory.

2. Run the Django development server.
   
3. Open your web browser and navigate to `http://localhost:8000`.

4. Enter the name of a city in the input field and click the "Search" button.

5. The webpage will display the current weather information for the specified city, including temperature, humidity, wind speed, and weather conditions.

## Dependencies

- Python 3.x
- Django (Python web framework)

## Resources

- [OpenWeather API Documentation](https://openweathermap.org/api)
- [Django Documentation](https://docs.djangoproject.com/)
