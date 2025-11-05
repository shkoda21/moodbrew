# Create your views here.
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer
from .utils import recommend_from_queryset
from . import services
from .forms import DrinkRecommendationForm

def moodbrew_home(request):
    recommendation = None
    form = DrinkRecommendationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        api_url = request.build_absolute_uri("/api/recommend/")
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            recommendation = response.json()

    return render(request, "index.html", {"form": form, "recommendation": recommendation})

@api_view(['GET'])
def list_drinks(request):
    drinks = Drink.objects.all()

    mood = request.GET.get('mood')
    weather = request.GET.get('weather')
    category = request.GET.get('category')
    time_of_day = request.GET.get('time_of_day')
    season = request.GET.get('season')

    if category:
        drinks = drinks.filter(category__iexact=category)
    if mood:
        drinks = drinks.filter(moods__icontains=mood)
    if weather:
        drinks = drinks.filter(weather__icontains=weather)
    if time_of_day:
        drinks = drinks.filter(time_of_day__icontains=time_of_day)
    if season:
        drinks = drinks.filter(season__icontains=season)

    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def recommend(request):
    """
    POST payload can include:
    {
      "mood": "cozy",
      "weather": "rainy",         # optional
      "time_of_day": "evening",
      "season": "summer",
      "city": "New York"           # optional - used to auto-fetch weather if 'weather' not provided
    }
    """
    data = request.data
    mood = data.get('mood')
    weather = data.get('weather')
    time_of_day = data.get('time_of_day')
    season = data.get('season')
    city = data.get('city')

    # If weather not provided, try to fetch from city
    if not weather and city:
        fetched = services.get_weather_condition_for_city(city)
        # fetched may be None if missing API key / error
        if fetched:
            weather = fetched

    qs = Drink.objects.all()
    recommendation = recommend_from_queryset(qs, mood=mood, weather=weather,
                                           time_of_day=time_of_day, season=season)
    if recommendation:
        serializer = DrinkSerializer(recommendation)
        return Response(serializer.data)
    return Response({'message': 'No matching drink found.'}, status=status.HTTP_404_NOT_FOUND)

def recommend_form_view(request):
    return render(request, "recommend_form.html")