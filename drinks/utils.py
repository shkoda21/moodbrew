import random

def score_drink(drink, mood=None, weather=None, time_of_day=None, season=None):
    score = 0
    if mood and mood in (drink.moods or []): score += 2
    if weather and weather in (drink.weather or []): score += 1
    if time_of_day and time_of_day in (drink.time_of_day or []): score += 1
    if season and season in (drink.season or []): score += 1
    return score

def recommend_from_queryset(qs, mood=None, weather=None, time_of_day=None, season=None):
    scored = []
    for drink in qs:
        s = score_drink(drink, mood, weather, time_of_day, season)
        if s > 0:
            scored.append((s, drink))
    if not scored:
        return None
    scored.sort(key=lambda x: x[0], reverse=True)
    top_score = scored[0][0]
    top = [d for sc, d in scored if sc == top_score]
    return random.choice(top)
