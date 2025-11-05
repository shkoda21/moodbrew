from django import forms

class DrinkRecommendationForm(forms.Form):
    MOOD_CHOICES = [
        ('cozy', 'Cozy'),
        ('energized', 'Energized'),
        ('romantic', 'Romantic'),
        ('lazy', 'Lazy'),
        ('stressed', 'Stressed'),
        ('focused', 'Focused'),
        ('calm', 'Calm'),
        ('thoughtful', 'Thoughtful'),
        ('fresh', 'Fresh'),
        ('relaxed', 'Relaxed'),
        ('sleepy', 'Sleepy'),
        ('comforted', 'Comforted'),
        ('motivated', 'Motivated'),
        ('tired', 'Tired'),
        ('chill', 'Chill'),
        ('happy', 'Happy'),
        ('carefree', 'Carefree'),
        ('nostalgic', 'Nostalgic'),
        ('rebellious', 'Rebellious'),
        ('bold', 'Bold'),
        ('reflective', 'Reflective'),
        ('joyful', 'Joyful'),
        ('melancholic', 'Melancholic'),
        ('warm', 'Warm'),
        ('creative', 'Creative'),
    ]

    WEATHER_CHOICES = [
        ('sunny', 'Sunny'),
        ('rainy', 'Rainy'),
        ('cold', 'Cold'),
        ('cloudy', 'Cloudy'),
    ]

    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]

    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('Fall', 'Fall'),
        ('winter', 'Winter'),
    ]

    mood = forms.ChoiceField(choices=MOOD_CHOICES, label="Mood")
    weather = forms.ChoiceField(choices=WEATHER_CHOICES, label="Weather")
    time_of_day = forms.ChoiceField(choices=TIME_CHOICES, label="Time of Day")
    season = forms.ChoiceField(choices=SEASON_CHOICES, label="Season")