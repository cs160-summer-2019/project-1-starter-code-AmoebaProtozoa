from django.shortcuts import render
from django.http import HttpResponse

def forecast(request):
    return render(request, 'weather/forecast.html')

def forecast_alert(request):
    return render(request, 'weather/forecast-alert.html')

def comparison(request):
    return render(request, 'weather/comparison.html')
  
def comparison_alt(request):
    return render(request, 'weather/comparison-alt.html')

def comparison_alert(request):
    return render(request, 'weather/comparison-alert.html')

def index(request):
    return render(request, 'weather/index.html')

def forecast_week(request):
  return render(request, 'weather/forecast-week.html')

def forecast_week_alert(request):
  return render(request, 'weather/forecast-week-alert.html')

def forecast_month(request):
  return render(request, 'weather/forecast-month.html')

def forecast_month_alert(request):
  return render(request, 'weather/forecast-month-alert.html')