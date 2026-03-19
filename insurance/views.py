from django.shortcuts import render, redirect
from .models import Worker, InsurancePlan
from .forms import WorkerForm, InsurancePlanForm
import requests

def dashboard(request):

    workers = Worker.objects.all()
    plans = InsurancePlan.objects.count()

    cities = set()

    for worker in workers:
        cities.add(worker.city)

    city_weather = []

    for city in cities:

        temp, weather = get_weather(city)

        city_weather.append({
            "city": city,
            "temperature": temp,
            "weather": weather
        })

    context = {
        "workers": workers.count(),
        "plans": plans,
        "city_weather": city_weather
    }

    return render(request, "dashboard.html", context)
def workers_list(request):

    workers = Worker.objects.all()

    worker_data = []

    for worker in workers:

        status, risk = calculate_risk(worker.city)

        worker_data.append({
            "id": worker.id,
            "name": worker.name,
            "city": worker.city,
            "platform": worker.platform,
            "daily_income": worker.daily_income,
            "plan": worker.plan,
            "risk_status": status,
            "risk_percent": risk
        })

    return render(request, "workers.html", {"workers": worker_data})
def plans_list(request):
    plans = InsurancePlan.objects.all()
    return render(request, "plans.html", {"plans": plans})


def add_worker(request):

    if request.method == "POST":
        form = WorkerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('workers')

    else:
        form = WorkerForm()

    return render(request, "add_worker.html", {"form": form})


def add_plan(request):

    if request.method == "POST":
        form = InsurancePlanForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('plans')

    else:
        form = InsurancePlanForm()

    return render(request, "add_plan.html", {"form": form})
def edit_worker(request, id):

    worker = Worker.objects.get(id=id)

    if request.method == "POST":
        form = WorkerForm(request.POST, instance=worker)

        if form.is_valid():
            form.save()
            return redirect('workers')

    else:
        form = WorkerForm(instance=worker)

    return render(request, "edit_worker.html", {"form": form})
def delete_worker(request, id):

    worker = Worker.objects.get(id=id)
    worker.delete()

    return redirect('workers')
def edit_plan(request, id):

    plan = InsurancePlan.objects.get(id=id)

    if request.method == "POST":
        form = InsurancePlanForm(request.POST, instance=plan)

        if form.is_valid():
            form.save()
            return redirect('plans')

    else:
        form = InsurancePlanForm(instance=plan)

    return render(request, "edit_plan.html", {"form": form})
def delete_plan(request, id):

    plan = InsurancePlan.objects.get(id=id)
    plan.delete()

    return redirect('plans')
def get_weather(city):

    api_key = "c02ab3ce26acd3abe93e03e48a4d949b"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    print("Weather API:", data)

    if response.status_code == 200 and "main" in data:

        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]

    else:

        temp = "N/A"
        weather = "Unavailable"

    return temp, weather



def get_air_quality(lat, lon):

    api_key = "c02ab3ce26acd3abe93e03e48a4d949b"

    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    print("AQI API:", data)

    if response.status_code == 200 and "list" in data:

        aqi = data["list"][0]["main"]["aqi"]

    else:

        aqi = "N/A"

    return aqi
def calculate_risk(city):

    # Get weather data
    temp, weather = get_weather(city)

    # Example coordinates for Hyderabad
    # In a real system we would map city → lat/lon
    lat = 17.3850
    lon = 78.4867

    aqi = get_air_quality(lat, lon)

    risk = 0

    # Heat Risk
    if temp != "N/A":
        if temp >= 45:
            risk += 40
        elif temp >= 38:
            risk += 25

    # Rain Risk
    if weather == "Rain":
        risk += 30

    # Pollution Risk
    if aqi != "N/A":
        if aqi >= 5:
            risk += 30
        elif aqi >= 4:
            risk += 20

    # Decide risk status
    if risk >= 60:
        status = "High"
    elif risk >= 30:
        status = "Medium"
    else:
        status = "Low"

    return status, risk