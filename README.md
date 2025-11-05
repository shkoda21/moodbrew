# MoodBrew (Django + DRF skeleton)
A simple Django + Django REST Framework project that brews drink recommendations based on mood, time of day, season, and weather.
(Note: Works with or without live weather data.)

## Setup

1. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt

2. (Optional) Create a .env file in the project root
Add your environment variables:
SECRET_KEY="your_secret_key_here"
DEBUG=True   # or False for production
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: OpenWeatherMap API key for live weather-based recommendations
OPENWEATHER_API_KEY="your_api_key_here"

3. Apply database migrations:
python manage.py makemigrations
python manage.py migrate

4. Create superuser (for Django admin access):
python manage.py createsuperuser

5.(Optional)Load sample drinks data:
You can load example drinks data using:
python manage.py loaddrinks

Or manually add your own dataset using the Django Admin panel at:
http://127.0.0.1:8000/admin/

Example drink entry:

name: "Spiced Chai Latte"
category: "tea"
description: "Warm and soothing..."
moods: ["cozy", "relaxed"]
weather: ["rainy", "cold"]
time_of_day: ["afternoon", "evening"]
season: ["fall", "winter"]

6. Run the development server:
python manage.py runserver

Visit:
http://127.0.0.1:8000/

## API Endpoints

| Endpoint          | Method | Description                                                |
| ----------------- | ------ | ---------------------------------------------------------- |
| `/api/drinks/`    | `GET`  | List all drinks                                            |
| `/api/recommend/` | `POST` | Get drink recommendation based on user input               |
| `/api/form/`      | `GET`  | Front-end demo form that uses weather + mood               |
| `/`               | `GET`  | Basic HTML form for mood-based recommendation (no weather) |

Example request — /api/recommend/
{
  "mood": "cozy",
  "time_of_day": "evening",
  "season": "summer",
  "city": "New York"
}
If city is provided and OPENWEATHER_API_KEY is set,
the app will automatically fetch current weather conditions from OpenWeatherMap.

## How It Works

When a user submits their mood, time of day, season, and optionally a city the app generates a personalized drink recommendation.

1. Weather Check (Optional) —
If the user includes a city and your OPENWEATHER_API_KEY is set, the app fetches the current weather from OpenWeatherMap to use as part of the recommendation.

2. Drink Scoring —
Each drink in the database receives a score based on how closely it matches the user’s context:

+2 points if the mood matches
+1 point for matching weather
+1 point for matching time of day
+1 point for matching season

If mood is missing or doesn’t match, the algorithm still works — just with less weight on that factor.

3. Recommendation Logic —
The drinks with the highest scores are considered top matches.
If multiple drinks share the top score, one is chosen randomly for variety.

This makes the system flexible: it works with structured form input (like in /api/form/) or raw JSON requests to /api/recommend/, adapting intelligently to the user’s input.